import numpy as np
from glob import glob
import os
import cv2

dataset_input = "./input"
dataset_output = "./output"
label_input = os.path.join( dataset_input  , "labels" )
label_output = os.path.join( dataset_output , "labels" )

def mkdir_p(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

mkdir_p(dataset_output)
mkdir_p(label_output)

label_names = sorted(glob(label_input+"/*"))
count =0
for label_name0 in label_names:
    print(label_name0)
    with open(label_name0, "r") as f0:
        labels0 = f0.readlines()
    coords=[]
    for label in labels0:
        coord = label.split()
        coords.append(coord)
    label_name = os.path.join( label_output , os.path.splitext(os.path.basename(label_name0))[0]+".txt" )
    file_label = open(label_name, "w")
    for coord in coords:
        category, x, y, w, h = coord
        label = coord
        if(category == "1" and count<6000):
            count= count+1
            print("delete!")
        else:
            file_label.write(" ".join( [str(l) for l in label] ) + "\n")
    file_label.close()       
    

            