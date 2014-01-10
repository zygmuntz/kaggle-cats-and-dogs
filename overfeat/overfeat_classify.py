#!/usr/bin/env python

"Set your paths below"

import os
from glob import glob

input_dir = '/path/to/kaggle-dogs-vs-cats/data/train/'
output_dir = '/path/to/kaggle-dogs-vs-cats/data/overfeat_predictions_train/'
overfeat = '/path/to/overfeat/bin/linux/overfeat'
overfeat_data_dir = '/path/to/overfeat/data/default/'

files = glob( input_dir + '*.jpg' )
files.sort()

for f in files:
	print f
	basename = os.path.basename( f )
	
	cmd = '{} -l -d {} {} > {}{}.txt'.format( overfeat, overfeat_data_dir, f, output_dir, basename )
	#print cmd
	os.system( cmd )
	
