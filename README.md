
scrapeur.py
======================

Scrapeur is a Python script for scraping emails, by parsing web pages.

Released under GNU General Public Licence

Requirements
======================
* sys
* argparse
* re
* urllib2
* csv

Instructions
======================

Run scrapeur.py with arguments

```
python scrapeur.py -h

arguments:
  -h, --help     show this help message and exit
  -i INPUT_PATH  path to the csv file with urls
  -o OUT         out file for saving data

```

To do
======================
* scrap a single url by passing it in
* ~~add a user-agent~~
* scrap website with login authentification
* scrap specific content (XPath or CSSSelectors)
