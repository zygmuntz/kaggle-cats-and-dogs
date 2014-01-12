#!/usr/bin/env python

"""
Produce a predictions file for Kaggle from OverFeat predictions on test images
Set your paths below
"""

import os
import csv
import random
from glob import glob

#

cats_file = 'data/cats.txt'
dogs_file = 'data/dogs.txt'
predictions_dir = 'data/overfeat_predictions_test/'
output_file = 'data/predictions.csv'

# load cat and dog names

cf = open( cats_file )
df = open( dogs_file )

cats = cf.read()
cats = cats.split( "\n" )
cats = { x: x for x in cats }

dogs = df.read()
dogs = dogs.split( "\n" )
dogs = { x: x for x in dogs }

#

files = glob( predictions_dir + '*.txt' )
# sort in proper order; this assumes names like "xxxx.jpg.txt"
files = sorted( files, key = lambda x: int( x.split( "/" )[-1].split(".")[-3] ))

writer = csv.writer( open( output_file, 'wb' ))
writer.writerow( [ 'id', 'label' ] )

counter = 0

for f in files:
	counter += 1
	print f
	
	pf = open( f )
	predictions = pf.read()
	predictions = predictions.split( "\n" )
	predictions = map( lambda x: x.split( "0." )[0].strip(), predictions )
	if predictions[-1] == '':
		predictions.pop()
		
	predicted_class = ''
	for p in predictions:
		if p in cats:
			predicted_class = '0'
			break
		if p in dogs:
			predicted_class = '1'
			break
	
	#print "{}\t{}".format( true_class, predicted_class )
	if not predicted_class:
		predicted_class = random.choice(( '0', '1' ))

	writer.writerow( [ counter, predicted_class ] )
	



















	
