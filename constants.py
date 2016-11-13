from urllib.parse import quote_plus

# Query
query_raw = "tissue cryopreservation"

# Number of papers.  Change this to the actual number for the given search term
papers = 10288

##################################################
# You shouldn't need to change beyond this point #
##################################################

# URL encode query
query = quote_plus(query_raw)

# This is the maximum page size allowed.  Don't change this
page_size = 100

# Compute the number of pages that there will be
num_pages = papers // page_size + 1
