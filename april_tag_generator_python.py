#!/usr/bin/python
import numpy as np
import cv2

def mainFunction():
	maximumValue = 68719476735
	mean = maximumValue // 2
	nominalValue = 2863311530
	deviation = mean // 2
	numberOfImages = 1
	choice = 255
	startValue = 2863311530
	endValue = startValue + 1
	tagLength = 240
	imageSize = 640
	backgroundImage = []
	angles = 0
	rawAngles = []
	filePath = 'G:\\Ubuntu\\apriltags\\'
	fileName = 'output'
	#backgroundFilename = 'G:\\Ubuntu\\apriltag_generator_python\\apriltag_generator_python\\background.jpg'
	backgroundFilename = 'background.jpg'
	isBackgroundLoaded = False
	isBackgroundApplied = False
	while choice:
		displayMenu()
		choice_string = input("Enter choice: ")
		choice = int(choice_string)
		if choice == 0:	
			print(choice)
		elif choice == 1:
			if angles == 0:
				for i in range(startValue, endValue):
					temporary = generateArray(i)
					temporary = generateImageValues(temporary)
					output = generateImage(temporary, tagLength, imageSize, angles, backgroundImage, isBackgroundApplied)
					saveImage(output, filePath, fileName, i, angles)
			else:
				for j in range(len(angles)):
					for i in range(startValue, endValue):
						temporary = generateArray(i)
						temporary = generateImageValues(temporary)
						output = generateImage(temporary, tagLength, imageSize, angles[j], backgroundImage, isBackgroundApplied)
						saveImage(output, filePath, fileName, i, angles[j])
		elif choice == 2:
			startValue = input('Enter start value: ')
			startValue = int(startValue)
		elif choice == 3:
			endValue = input('Enter end value: ')
			endValue = int(endValue)
		elif choice == 4:
			print('Current filename: ', fileName)
			fileName = input('Enter new filename: ')
			print('New filename: ', fileName)
		elif choice == 5:
			print('Current file path: ', filePath)
			filePath = input('Enter new file path: ')
			print('New file path: ', filePath)
		elif choice == 6:
			for i in range(0, numberOfImages):
				k = np.random.normal(mean, deviation)
				k = int(k)
				if angles == 0:
					temporary = generateArray(k)
					temporary = generateImageValues(temporary)
					output = generateImage(temporary, tagLength, imageSize, angles, backgroundImage, isBackgroundApplied)
					saveImage(output, filePath, fileName, k, angles)
				else:
					for j in range(len(angles)):
						temporary = generateArray(k)
						temporary = generateImageValues(temporary)
						output = generateImage(temporary, tagLength, imageSize, angles[j], backgroundImage, isBackgroundApplied)
						saveImage(output, filePath, fileName, k, angles[j])
		elif choice == 7:
			print('Current mean: ', mean)
			mean = input('Enter new mean: ')
			mean = int(mean)
			print('New mean: ', mean)			
		elif choice == 8:
			print('Current deviation: ', deviation)
			deviation = input('Enter new deviation: ')
			deviation = int(deviation)
			print('New deviation: ', deviation)
		elif choice == 9:
			print('Current current number of images: ', numberOfImages)
			numberOfImages = input('Enter new number of images: ')
			numberOfImages = int(numberOfImages)
			print('New number of images: ', numberOfImages)
		elif choice == 10:
			print('Current angles: ', angles)
			rawAngles = input('Enter angles: ')
			rawAngles = rawAngles.split(',')
			rawAngles = [int(i) for i in rawAngles]
			angles = rawAngles
			print('New angles: ', angles)
		elif choice == 11:
			if isBackgroundApplied:
				isBackgroundApplied = False
				print('Background image off.')
			else:
				if isBackgroundLoaded:
					isBackgroundApplied = True
				else:
					#backgroundImage = cv2.imread(backgroundFilename, cv2.IMREAD_COLOR)
					backgroundImage = cv2.imread(backgroundFilename, cv2.IMREAD_GRAYSCALE)
					isBackgroundLoaded = True
					isBackgroundApplied = True
				print('Background image on.')
		elif choice == 12:
			print('Current background: ', backgroundFilename)
			backgroundFilename = input('Enter new background image: ')
			print('New background file: ', backgroundFilename)
		elif choice == 13:
			print('Current tag length: ', tagLength)
			tagLength = input('Enter new tag length: ')
			tagLength = int(tagLength)
			print('New tag length: ', tagLength)
		elif choice == 14:
			print('Current image size: ', imageSize)
			imageSize = input('Enter new image size: ')
			imageSize = int(imageSize)
			print('New image size: ', imageSize)
		elif choice == 15:
			printHelp()
		elif choice == 16:
			print(choice)
		else:
			print(choice)
	return	
	
def displayMenu():
	header = "-" * 40
	print(header)
	print("|>>>Menu<<<".ljust(39) + '|')
	print("|0. Exit".ljust(39) + '|')
	print("|1. Generate sequential images".ljust(39) + '|')
	print("|2. Change start value".ljust(39) + '|')
	print("|3. Change end value".ljust(39) + '|')
	print("|4. Change filename".ljust(39) + '|')
	print("|5. Change file path".ljust(39) + '|')
	print("|6. Generate normal images".ljust(39) + '|')
	print("|7. Change mean".ljust(39) + '|')
	print("|8. Change deviation".ljust(39) + '|')
	print("|9. Change number of images".ljust(39) + '|')
	print("|10. Rotation angles".ljust(39) + '|')
	print("|11. Apply/remove background".ljust(39) + '|')
	print("|12. Assign background image".ljust(39) + '|')
	print("|13. Adjust tag length".ljust(39) + '|')
	print("|14. Adjust image size".ljust(39) + '|')
	print("|15. Help".ljust(39) + '|')
	print("|16. Settings".ljust(39) + '|')
	print(header)
	return
	
def generateImage(input_array, tag_width, image_width, image_angle, background_image, apply_background = False):
	print("generateImage()")
	maximumPixelStrength = 255
	halfMaximumPixelStrength = 124	
	output = np.array(input_array, dtype = np.float32)
	a = output.shape[0]
	b = output.shape[1]
	output = np.multiply(output, maximumPixelStrength)
	while a < tag_width:
		output = output.astype(np.float32)
		output = np.multiply(output, 1.0 / maximumPixelStrength)
		a *= 2
		b *= 2
		output = cv2.resize(output, (a, b))
		output = np.multiply(output, maximumPixelStrength)  
		output = np.rint(output)
		output = output.astype(np.uint8)
		retval, output = cv2.threshold(output, halfMaximumPixelStrength, maximumPixelStrength, cv2.THRESH_BINARY)
	borderSize = image_width - tag_width
	borderSize = borderSize // 2
	if apply_background:
		background_image = cv2.resize(background_image, (image_width, image_width))
		borderSize = image_width - tag_width
		borderSize = borderSize // 2
		background_image[borderSize : borderSize + output.shape[0], borderSize : borderSize + output.shape[1]] = output
		output = background_image
	else:	
		if image_width - tag_width > 0:
			output = cv2.copyMakeBorder(output, top = borderSize, bottom = borderSize, left = borderSize, right = borderSize, borderType = cv2.BORDER_CONSTANT, value = [0, 0, 0])
	centerLocation = (image_width / 2, image_width / 2)	
	rotationMatrix = cv2.getRotationMatrix2D(centerLocation, image_angle, 1.0)
	output = cv2.warpAffine(output, rotationMatrix, (image_width, image_width))
	cv2.imshow('Apriltag', output)
	cv2.waitKey(300)
	return output
	
def generateArray(tag_number):
	print("generateArray()")
	apriltagArrayLength = 6
	baseNumber = 2
	n = apriltagArrayLength
	m = apriltagArrayLength
	output = [[False] * m for i in range(n)]
	divisor = baseNumber
	temporary = tag_number
	for i in range(len(output)):
		for j in range(len(output[i])):
			if temporary % divisor > 0:
				output[i][j] = False
			else:
				output[i][j] = True
			temporary = temporary // divisor
	#for row in output:
	#	for element in row:
	#		print(element, end = ' ')
	#	print()
	return output
		
def generateImageValues(boolean_array):
	apriltagWidth = 10
	apriltagHeight = 10
	n = apriltagWidth
	m = apriltagHeight
	output = [[0] * m for i in range(n)]
	for i in range(len(output)):
		for j in range(len(output[i])):
			onBorder = False
			output[i][j] = 1.0
			if i == 1 and j != 0 and j != apriltagWidth - 1:
				output[i][j] = 0
				onBorder = True
			elif i == (apriltagWidth - 1) - 1 and j != 0 and j != apriltagWidth - 1:
				output[i][j] = 0
				onBorder = True
			elif j == 1 and i != 0 and i != apriltagWidth - 1:
				output[i][j] = 0
				onBorder = True
			elif j == (apriltagWidth - 1) - 1 and i != 0 and i != apriltagWidth - 1:
				output[i][j] = 0
				onBorder = True

			if i == 0 or i == apriltagWidth - 1:
				onBorder = True
			elif j == 0 or j == apriltagWidth - 1:
				onBorder = True
				
			if not onBorder:
				if boolean_array[i - 2][j - 2]:
					output[i][j] = 1.0
				else:
					output[i][j] = 0.0
	return output
	
def saveImage(image_array, file_path, file_name, image_number, image_rotation):
	fileName = file_path + file_name + '_' + str(image_number) + '_' + str(image_rotation) + '.jpg'
	cv2.imwrite(fileName, image_array)
	

def printHelp():
	print("(0) Exit - Exit application")
	print("(1) Generate sequential images - Create images from start value to end value")
	print("(2) Change start value - Change start value")
	print("(3) Change end value - Change end value")
	print("(4) Change filename - Change filename under which images are stored")
	print("(5) Change file path - Change the path under which images are stored")
	print("(6) Generate normal images - Create images with a random value of normal distribution")
	print("(7) Change mean - Change mean which is is used for generating normal image distribution")
	print("(8) Change deviation - Change standard deviation of normal image distribution")
	print("(9) Change number of images - Change the number of images generated with (6)")
	print("(10) Rotation angles - Enter the angles at which the Apriltags will be rotated")
	print("(11) Apply/remove background - Apply or remove the current background image")
	print("(12) Assign background image -  Change filename of background image")
	print("(13) Adjust tag lengt - Change the length of the Apriltag image")
	print("(14) Adjust image size - Change the size of the image which contains the Apriltag")
	print("(15) Help - Display information on selections")
	print("(16) Settings - Display current settings")
	
if __name__ == "__main__":
	mainFunction()	
	
