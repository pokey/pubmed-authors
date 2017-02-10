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
   pip3 install -e .
   ```

Running on OS X
---------------

Run

```
pubmed_authors tissue cryopreservation
```

The output will be in `out.csv`.

Credits
-------
This package was created with
[Cookiecutter](https://github.com/audreyr/cookiecutter-pypackage).
