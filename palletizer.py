
#the following imports the necessary libraries make sure you have numpy,matplotlib and sklearn installed.
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import sklearn
from sklearn import cluster
import numpy as np
from PIL import Image

#Opens to file into an Image Object

old_file=input('What is the png you want to palletize (drop the .png): ')
new_file_name=input('Where do you want to save the modified image(drop the .png)?: ')
palletized_txt_name=input('Where do you want to save the palletized labels(drop the file extension): ')
pallete_file=input('Where do you want to save the pallete(drop the file extension)?: ')
color_number=int(input('How many colors do you want?: '))

im=Image.open(old_file+'.png')
im.convert('RGBA')


#converts the image to a pixel
list_=[]
for x in range(im.size[0]):
	for y in range(im.size[1]):
		list_.append(list(im.getpixel((x,y))[:3]))

#Performs KMeans Clustering
print('Doing KMeans Clustering...')
kmean=cluster.KMeans(n_clusters=color_number).fit(list_)
print('...Finished KMeans Clustering')

#Make a new image and file to save the picture and file
new_image = Image.new('RGB', im.size, color='white')
new_file= open(new_file_name+'.txt','w')

#Gets the labels and cluster centers (which become the pallete)
labels=np.array(kmean.labels_)
centers=np.array(kmean.cluster_centers_,dtype='uint8');

#Makes the new image and file based on the pallete
for x in range(im.size[0]):
	for y in range(im.size[1]):
		new_image.putpixel((x,y),tuple(centers[labels[x*im.size[1]+y]]))
		new_file.write('%d\n'%(labels[x*im.size[1]+y]))
new_file.close()
new_image.save(new_file_name+'.png')

#Saves the cluster centers as the pallete
new_pallete=open(pallete_file+'.txt','w')
for i in range(len(centers)):
	new_pallete.write(('%02x%02x%02x\n')%(centers[i][0],centers[i][1],centers[i][2]))

new_pallete.close()