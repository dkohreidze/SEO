# seo automatic internal links script

A super simple Python script that creates HTML links around your keywords for all text files in the working directory.

The script goes through all .txt files in its directory and inserts an `<a>` tag around the first instance of your keyword to its corresponding URL. Only exact keyword matches (case sensitive) will be linked. 

Use a CSV file named keywords.csv to hold your keyword, URL pairs.

Bugs or feature requests? Please file an issue.

To run this script: 
* Place the .txt files you want to crawl in the same directory as the script file. (I recommend placing everything in a new folder, as this script will edit all text files within the current directory)
* On Mac, open Terminal and `cd` into your working directory 
* Exectute the script with the command `python sail.py`
