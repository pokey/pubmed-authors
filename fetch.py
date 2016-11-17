from urllib.parse import urlencode

from bs4 import BeautifulSoup
import grequests
import requests

# This is the maximum page size allowed.  Don't change this
page_size = 100
max_concurrent = 20
max_attempts = 5

# Generate url to search for papers
def _get_search_url(term):
    query = urlencode(dict(
        db='pubmed',
        term=term,
        usehistory='y'
    ))
    return ('https://eutils.ncbi.nlm.nih.gov/'
            'entrez/eutils/esearch.fcgi?{}').format(query)


# Generate url to fetch info about papers
def _get_fetch_url(webenv, query_key, paper_idx):
    query = urlencode(dict(
        db='pubmed',
        query_key=query_key,
        WebEnv=webenv,
        retmode='xml',
        retmax=str(page_size),
        retstart=str(paper_idx)
    ))
    return ('https://eutils.ncbi.nlm.nih.gov/'
            'entrez/eutils/efetch.fcgi?{}').format(query)


# Fetches results and yields them
class Fetcher(object):

    def __init__(self, term):
        self.term = term

    # Total number of papers
    @property
    def total(self):
        return self.num_papers

    # Do initial search to get list of papers
    def search(self):
        r = requests.get(_get_search_url(self.term))
        soup = BeautifulSoup(r.text, "lxml")

        self.webenv = soup.webenv.string
        self.query_key = soup.querykey.string
        self.num_papers = int(soup.count.string)

    # Yield info about the papers
    def get_pages(self):
        # Urls to fetch papers |page_size| at a time
        urls = [
            _get_fetch_url(self.webenv, self.query_key, paper_idx)
            for paper_idx in range(0, self.num_papers, page_size)
        ]

        # Keep track of failed requests here to try again
        failed_urls = []

        # Don't try more than max_attempts times
        attempts = 0

        # Keep iterating through urls until all have succeeded
        while len(urls) > 0:
            if attempts == max_attempts:
                raise Exception("Too many failures")

            rs = (
                grequests.get(url)
                for url in urls
            )

            # Execute the requests and yield the results as xml
            # Note that the |size| parameter is used to throttle requests so server doesn't
            # shut us down
            for r in grequests.imap(rs, size=max_concurrent):
                if r.status_code != 200:
                    failed_urls.append(r.request.url)
                else:
                    yield r.text

            urls = failed_urls
            failed_urls = []
            attempts += 1
