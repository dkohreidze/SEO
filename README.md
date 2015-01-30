# seo automatic internal links script

##`sail.py`

This Python script inserts HTML anchor text links within a text file on your local machine.

The script reads all .txt files in it's directory and inserts anchor text links around the first instance of your keyword to its corresponding URL.

All keyword/URL pairs must be placed into the script in the format provided. You may add any number of keyword/URL pairs.

Currently the script is pretty basic - only exact keyword matches will be linked and you have to emuerate every keyword/URL pair into the code of the script. I plan to update it to be more versatile: accept additional data files (CSV, XML, etc.) and provide link customization options (target & nofollow attributes). If you have any feature requests, please file an issue in github.


To run this script: 
* Place the .txt files you want to crawl in the same directory as the script file. (I recommend placing everything in a new folder, as this script will edit all text files within the current directory)
* On Mac, open Terminal and `cd` into your working directory 
* Exectute the script with the command `python sail.py`
