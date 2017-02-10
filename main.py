import csv
import sys
import asyncio
from asyncio import as_completed

from bs4 import BeautifulSoup
from tqdm import tqdm
import aiohttp

from pubmedasync.fetch import Fetcher
from pubmedasync.process import extract_authors, fieldnames

# Get term from command-line args
term = " ".join(sys.argv[1:])


# Get list of results
async def main():
    conn = aiohttp.TCPConnector(limit=10)
    async with aiohttp.ClientSession(connector=conn) as session:
        fetcher = Fetcher(session, term)
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

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
