import csv
import sys
from asyncio import as_completed

import aiohttp
from bs4 import BeautifulSoup
from pubmedasync.fetch import Fetcher
from tqdm import tqdm

from pubmed_authors.process import extract_authors, fieldnames


# Get list of results
async def run(query):
    conn = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=conn) as session:
        fetcher = Fetcher(session, query)
        await fetcher.search()

        # Iterate through all the pages and extract all authors
        results = []
        with tqdm(total=fetcher.total, unit='paper') as pbar:
            for data in as_completed(fetcher.get_pages()):
                soup = BeautifulSoup(await data, "lxml")
                papers = soup.find_all('pubmedarticle')

                for paper in papers:
                    results += extract_authors(paper)

                # Update progress bar
                pbar.update(len(papers))

        # Output information to csv file
        with open('out.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for result in results:
                writer.writerow(result)
