import re

# Field names for output csv
fieldnames = ['foreName', 'lastName', 'email',
              'affiliation1', 'affiliation2', 'affiliation3', 'affiliation4']

# Regex to extract email address
_email_re = re.compile(r"\b([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z0-9])\b")

# Helper function to handle case where author has less then 4 affiliations
def _get_affiliation(affiliations, idx):
    return affiliations[idx] if len(affiliations) > idx else ''

# Helper functino to handle case where author is lacking a name
def _getAttr(el, attr):
    ret = el.find(attr)
    return '' if ret == None else str(ret.string)

# Given an xml element representing an author, extract information
def extract_author(author):
    affiliations = [
        str(affiliation.string)
        for affiliation in author.find_all('affiliation')
    ]
    email = ''
    if len(affiliations) > 4:
        raise Exception("Too many affiliations")
    for affiliation in affiliations:
        emails = _email_re.findall(affiliation)
        if len(emails) > 0:
            email = emails[0]
    return dict(
        lastName=_getAttr(author, 'lastname'),
        foreName=_getAttr(author, 'forename'),
        affiliation1=_get_affiliation(affiliations, 0),
        affiliation2=_get_affiliation(affiliations, 1),
        affiliation3=_get_affiliation(affiliations, 2),
        affiliation4=_get_affiliation(affiliations, 3),
        email=email
    )
