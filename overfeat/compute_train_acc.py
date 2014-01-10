#!/usr/bin/env python

"Compute accuracy for train images"
"Shows predictions that are neither cats nor dogs"

import os
from glob import glob

cats_file = 'data/cats.txt'
dogs_file = 'data/dogs.txt'
predictions_dir = 'data/overfeat_predictions_train_orig/'

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
files.sort()

counter = 0
acc_counter = 0

for f in files:
	
	# true class
	basename = os.path.basename( f )
	true_class = basename.split( "." )[0]
	#print true_class
	
	pf = open( f )
	predictions = pf.read()
	predictions = predictions.split( "\n" )
	predictions = map( lambda x: x.split( "0." )[0].strip(), predictions )
	if predictions[-1] == '':
		predictions.pop()
		
	#print predictions

	predicted_class = ''
	for p in predictions:
		if p in cats:
			predicted_class = 'cat'
			break
		if p in dogs:
			predicted_class = 'dog'
			break
	
	#print "{}\t{}".format( true_class, predicted_class )
	if not predicted_class:
		print predictions

	counter += 1
	if true_class == predicted_class:
		acc_counter += 1

print		
print "{}/{}".format( acc_counter, counter )
print "accuracy: {}".format( 1.0 * acc_counter / counter )


	