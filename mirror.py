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
    coords = []
    for label in labels0:
        coord=  label.split()
        coords.append(coord)
        
    image_name = os.path.join( image_output , os.path.splitext(os.path.basename(image_name0))[0]+".jpg" )
    label_name = os.path.join( label_output , os.path.splitext(os.path.basename(image_name0))[0]+".txt" )    
    file_label = open(label_name,"w")
    for coord in coords:
        #category, x, y, w, h = coord
        label = coord
        file_label.write(" ".join( [str(l) for l in label] ) + "\n")
    cv2.imwrite(image_name,image0)
    file_label.close()
    
    #x flip
    image0 = cv2.cvtColor(image0, cv2.COLOR_BGR2RGB)
    image0_x =cv2.flip(image0, 1)
    
    image_name = os.path.join( image_output , os.path.splitext(os.path.basename(image_name0))[0]+"_x.jpg" )
    label_name = os.path.join( label_output , os.path.splitext(os.path.basename(image_name0))[0]+"_x.txt" )    
    file_label = open(label_name,"w")
    coords= []
    for label in labels0:
        coord = label.split()
        coords.append([coord[0], 1-float(coord[1]), coord[2], coord[3], coord[4]])
        
    for coord in coords:
        #category, x, y, w, h = coord
        label = coord
        file_label.write(" ".join( [str(l) for l in label] ) + "\n")
    cv2.imwrite(image_name,image0_x)
    file_label.close()
    
    #y flip
    image0_y = cv2.flip(image0, 0)
    image_name = os.path.join( image_output , os.path.splitext(os.path.basename(image_name0))[0]+"_y.jpg" )
    label_name = os.path.join( label_output , os.path.splitext(os.path.basename(image_name0))[0]+"_y.txt" )    
    file_label = open(label_name,"w")
    coords = []
    for label in labels0:
        coord = label.split()
        coords.append([coord[0], coord[1], 1-float(coord[2]), coord[3], coord[4]])
        
    for coord in coords:
        #category, x, y, w, h = coord
        label = coord
        file_label.write(" ".join( [str(l) for l in label] ) + "\n")
    cv2.imwrite(image_name,image0_y)
    file_label.close()
        