import numpy as np

# import open-cv library
import cv2

# here image is of class 'uint8', the range of values  
# that each colour component can have is [0 - 255]

# create a zero matrix of order 600x800 of 3-dimension
image = np.zeros((600, 800, 3),np.uint8)

# Painting the Red Strip 
image[:100,:,0] = 49;
image[:100,:,1] = 25;
image[:100,:,2] = 165;

# Painting the White Strip 
image[100:200,:,0] = 248;
image[100:200,:,1] = 245;
image[100:200,:,2] = 244;

# Painting the Blue Strip 
image[200:400,:,0] = 72;
image[200:400,:,1] = 44;
image[200:400,:,2] = 45;

# Painting the white Strip 
image[400:500,:,0] = 248;
image[400:500,:,1] = 245;
image[400:500,:,2] = 244;

# Painting the Red Strip 
image[500:600,:,0] = 49;
image[500:600,:,1] = 25;
image[500:600,:,2] = 165;

# Show the image formed
cv2.imshow("Thailand Flag",image);