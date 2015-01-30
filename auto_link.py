#!/usr/bin/python

import os
import re

links = {	 #keywords			#URLs
			'auto link' 	:	'https://github.com/dkohreidze/SEO'		,
			'Google'		:	'https://www.google.com'	
		}

#list files in dir
for fn in os.listdir('.'):
	if os.path.isfile(fn):
		if fn.endswith(".txt"):

			s = open(fn).read()

			print "Processing %s.." %fn

			for i in links:
				link = links[i]		

				s = re.sub(r'\b'+i+r'\b', '<a href="%s">%s</a>'%(link,i), s, 1)


			f = open(fn, 'w')
			f.write(s)
			f.close()

print "Complete."
	