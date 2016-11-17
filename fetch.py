from urllib.parse import urlencode

from bs4 import BeautifulSoup
import grequests
import requests

# This is the maximum page size allowed.  Don't change this
page_size = 200
max_concurrent = 5

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
def _get_fetch_url(webenv, query_key, page):
    query = urlencode(dict(
        db='pubmed',
        query_key=query_key,
        WebEnv=webenv,
        retmode='xml',
        retmax=str(page_size),
        retstart=str(page*page_size)
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

        # Compute the number of pages that there will be
        self.num_pages = self.num_papers // page_size + 1

    # Yield info about the papers
    def get_pages(self):
        # This generates the requests 
        rs = (
            grequests.get(_get_fetch_url(self.webenv, self.query_key, page))
            for page in range(self.num_pages)
        )

        # Execute the requests and yield the results as xml
        # Note that the |size| parameter is used to throttle requests so server doesn't
        # shut us down
        for r in grequests.imap(rs, size=max_concurrent):
            yield r.text
