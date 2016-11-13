import csv
import json
import re

from bs4 import BeautifulSoup

email_re = re.compile(r" ([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+).$")

def get_affiliation(affiliations, idx):
    return affiliations[idx] if len(affiliations) > idx else ''

def getAttr(el, attr):
    ret = el.find(attr)
    return '' if ret == None else str(ret.string)

def extract_author(author):
    affiliations = [
        str(affiliation.string)
        for affiliation in author.find_all('affiliation')
    ]
    email = ''
    for affiliation in affiliations:
        emails = email_re.findall(affiliation)
        if len(emails) > 0:
            email = emails[0]
    return dict(
        lastName=getAttr(author, 'lastname'),
        foreName=getAttr(author, 'forename'),
        affiliation1=get_affiliation(affiliations, 0),
        affiliation2=get_affiliation(affiliations, 1),
        affiliation3=get_affiliation(affiliations, 2),
        affiliation4=get_affiliation(affiliations, 3),
        email=email
    )

results = []
for i in range(103):
    with open('pages/{}.html'.format(i)) as f:
        data = f.read()
    soup = BeautifulSoup(data, "lxml")
    soup = BeautifulSoup(soup.pre.text, "lxml")
    results += [
        extract_author(author)
        for author in soup.find_all('author')
    ]

with open('out.csv', 'w') as csvfile:
    fieldnames = ['foreName', 'lastName', 'email', 'affiliation1',
                  'affiliation2', 'affiliation3', 'affiliation4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for result in results:
        writer.writerow(result)
