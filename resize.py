import numpy as np
from glob import glob
import os
import cv2

dataset_input = "./input"
dataset_output = "./output"
label_input = os.path.join( dataset_input  , "labels" )
image_input = os.path.join( dataset_input  , "images" )
image_output = os.path.join( dataset_output , "images" )
label_output = os.path.join( dataset_output , "labels" )
target_xsize = 3024
target_ysize = 4032


def mkdir_p(dirname):
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

mkdir_p(dataset_output)
mkdir_p(image_output)
mkdir_p(label_output)

image_names = sorted(glob(image_input+"/*"))

for image_name0 in image_names:
    print(image_name0)
    label_name = os.path.join( label_input , os.path.splitext(os.path.basename(image_name0))[0]+".txt" )
    with open(label_name,"r") as f0:
        labels0 = f0.readlines()
    image0 = cv2.imread(image_name0)
    height_image0, width_image0 = image0.shape[:2]
    rate_x = float(target_xsize / width_image0)
    rate_y = float(target_ysize / height_image0)
    print(rate_x)
    print(rate_y)
    coords = []
    for label in labels0:
        coord = label.split()
        coords.append([coord[0],    np.round(float(coord[1]), 6),    np.round(float(coord[2]),6),    np.round(float(coord[3])*rate_x,6),    np.round(float(coord[4])*rate_y, 6)])
    image0 = cv2.resize(image0, (target_xsize, target_ysize));
    
    image_name = os.path.join( image_output , os.path.splitext(os.path.basename(image_name0))[0]+".jpg" )
    label_name = os.path.join( label_output , os.path.splitext(os.path.basename(image_name0))[0]+".txt" )
    file_label = open(label_name,"w")
    for coord in coords:
        category, x, y, w, h = coord
        label = coord
        file_label.write(" ".join( [str(l) for l in label] ) + "\n")
    cv2.imwrite(image_name,image0)
