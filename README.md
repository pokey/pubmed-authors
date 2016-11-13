Installing on OS X
==================

1. Install [Homebrew](http://brew.sh/)
1. From a terminal, run

   ```
   brew install python3
   pip3 install -r requirements.txt
   ```

Running on OS X
===============

1. Run

   ```
   python3 fetch.py
   ```

   This will retrieve all the results in their raw xml format into the `pages`
   directory.  This sometimes fails with the following message:

   ```
   Traceback (most recent call last):
     File "fetch.py", line 126, in <module>
       f.write(soup.pre.text)
   AttributeError: 'NoneType' object has no attribute 'text'
   ```

   If so, run it again.  It might take a few tries.

1. Once this is successful, run 

   ```
   python3 process.py
   ```

   This will process all the files in the `pages` directory and put the output in
   `out.csv`


If you want to run it with a different search term, change `query_raw` and
`papers` in the file `constants.py`.
