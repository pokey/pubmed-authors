import csv
import sys

from bs4 import BeautifulSoup
from tqdm import tqdm

from fetch import Fetcher
from process import extract_author

# Get term from command-line args
term = " ".join(sys.argv[1:])

# Get list of results
fetcher = Fetcher(term)
fetcher.search()

# Iterate through all the pages and extract all authors
results = []
for data in tqdm(fetcher.get_pages(), total=fetcher.total):
    soup = BeautifulSoup(data, "lxml")
    results += [
        extract_author(author)
        for author in soup.find_all('author')
    ]

# Output information to csv file
with open('out.csv', 'w') as csvfile:
    fieldnames = ['foreName', 'lastName', 'email', 'affiliation1',
                  'affiliation2', 'affiliation3', 'affiliation4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow(result)
