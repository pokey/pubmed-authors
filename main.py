import csv
import sys

from bs4 import BeautifulSoup
from tqdm import tqdm

from fetch import Fetcher
from process import extract_author, fieldnames

# Get term from command-line args
term = " ".join(sys.argv[1:])

# Get list of results
fetcher = Fetcher(term)
fetcher.search()

# Iterate through all the pages and extract all authors
results = []
with tqdm(total=fetcher.total, unit='paper') as pbar:
    for data in fetcher.get_pages():
        soup = BeautifulSoup(data, "lxml")
        results += [
            extract_author(author)
            for author in soup.find_all('author')
        ]
        pbar.update(len(soup.find_all('pubmedarticle')))

# Output information to csv file
with open('out.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow(result)
