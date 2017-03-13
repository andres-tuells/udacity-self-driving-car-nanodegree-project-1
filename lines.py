import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2





def main():
	print("start")

	image = mpimg.imread('test_images/solidWhiteRight.jpg')

	#printing out some stats and plotting
	print('This image is:', type(image), 'with dimesions:', image.shape)
	plt.imshow(image)

	print("end")

if __name__=='__main__':
	main()