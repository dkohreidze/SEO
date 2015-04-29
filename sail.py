#!/usr/bin/python
# David Kohreidze

import os
import re

links = {	#keywords	#URLs
		'auto link' :  'https://github.com/dkohreidze/seo-auto-internal-links',
		'Google'    :  'https://www.google.com' # case sensitive Google
	}

for f in os.listdir('.'): # for every file in the current directory
  if os.path.isfile(f): # must be a file
    if f.endswith(".txt"): # must be a text file
	  s = open(f).read() # read file
	  print "Processing %s.." %f
	  
	  for i in links:
		s = re.sub(r'\b'+i+r'\b', '<a href="%s">%s</a>'%(links[i],i), s, 1)
	 
	  f = open(f, 'w')
	  f.write(s)
	  f.close()
print "Complete."