See [http://fastml.com/classifying-images-with-a-pre-trained-deep-network](http://fastml.com/classifying-images-with-a-pre-trained-deep-network/) for description.

	data/cats.txt - a list of "cat" ImageNet classes
	data/dogs.txt - a list of "dog" ImageNet classes
	data/overfeat_predictions_test.tar.gz - OverFeat predictions for the test set images
	data/overfeat_predictions_train.tar.gz - OverFeat predictions for the training images
	compute_train_acc.py - compute accuracy of the OverFeat predictions
	overfeat_classify.py - batch classification script
	predict.py - produce a file for Kaggle from OverFeat predictions on test images

You don't need to run `overfeat_classify.py` yourself, predictions are provided, both for the train and the test set.

This software is available under Doge General Public License (see LICENSE.txt).
