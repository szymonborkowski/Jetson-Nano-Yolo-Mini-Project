"""
This script was used to create annotations for the images taken from the below dataset.
This was done in attempt to create a new dataset for testing.
However, the original model was not able to detect the hand gestures in the dataset successfully.
This could have been due to overtraining of the original dataset.
"""


import os

filenames = sorted(os.listdir("./images/"))

filenames = [filename[:-4] for filename in filenames]

# dataset: https://www.kaggle.com/datasets/adamnovozmsk/hands

""" How new dataset classes map to training dataset:
circle -> ok
four -> four
one -> one 
thumb -> like
"""

# create a file for each picture
for filename in filenames:
    file = open('./labels/' + filename + '.txt', 'w')
    
    if "Circle" in filename:
        file.write("6 0.5 0.5 1.0 1.0")
    
    if "Four" in filename:
        file.write("3 0.5 0.5 1.0 1.0")
    
    if "One" in filename:
        file.write("7 0.5 0.5 1.0 1.0")
    
    if "Thumb" in filename:
        file.write("4 0.5 0.5 1.0 1.0")
    
    
    file.close()
