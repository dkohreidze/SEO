#!/usr/bin/python
# David Kohreidze

import csv
import os 
import re

with open('keywords.csv', 'rU') as csvf:
	reader = csv.reader(csvf)
	links = {rows[0]:rows[1] for rows in reader}

for f in os.listdir('.'):
  if os.path.isfile(f): 
    if f.endswith(".txt"): 
	  s = open(f).read()
	  print "Processing %s.." %f
	  for i in links:
		s = re.sub(r'\b'+i+r'\b', '<a href="%s">%s</a>' %(links[i],i), s, 1)
	  f = open(f, 'w')
	  f.write(s)
	  f.close()

print "Complete."