PubMed authors
=============

Uses [Entrez
api](https://www.ncbi.nlm.nih.gov/books/NBK25499/#chapter4.ESearch)
to search for authors publishing on a particular topic, and output a csv file
with information about the authors.

Installing on OS X
------------------

1. Install [Homebrew](http://brew.sh/)
1. From a terminal, run

   ```
   brew install python3
   pip3 install -r requirements.txt
   ```

Running on OS X
---------------

Run

```
python3 main.py tissue cryopreservation
```

The output will be in `out.csv`.
