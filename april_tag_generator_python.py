#!/usr/bin/python
import numpy as np
import cv2

def mainFunction():
	maximumValue = 68719476735
	mean = maximumValue // 2
	nominalValue = 2863311530
	choice = 12
	startValue = 0
	endValue = 0
	backgroundImage
	angles
	while choice:
		displayMenu()
		choice_string = input("Enter choice: ")
		choice = int(choice_string)
		if choice == 0:	
			print(choice)
		elif choice == 1:
			for i in range(startValue, endValue):
				temporary = generateArray(i)
				temporary = generateImageValues(temporary)
				generateImage(temporary)
		elif choice == 2:
			startValue = input('Enter start value: ')
			startValue = int(startValue)
		elif choice == 3:
			endValue = input('Enter end value: ')
			endValue = int(endValue)
		elif choice == 4:
			print(choice)
		elif choice == 5:
			print(choice)
		elif choice == 6:
			temporary = generateArray(nominalValue)
			temporary = generateImageValues(temporary)
			generateImage(temporary)
		elif choice == 7:
			print(choice)
		elif choice == 8:
			print(choice)
		elif choice == 9:
			print(choice)
		elif choice == 10:
			print(choice)
		elif choice == 11:
			print(choice)
		else:
			print(choice)
	return
	
	
def displayMenu():
	print("----Menu----")
	print("0. Exit")
	print("1. Generate sequential images")
	print("2. Change start value")
	print("3. Change end value")
	print("4. Change filename")
	print("5. Generate normal images")
	print("6. Change mean")
	print("7. Change deviation")
	print("8. Change number of images")
	print("9. Rotate")
	print("10. Apply background")
	print("11. Help")
	return
	
def generateImage(input_array):
	print("generateImage()")
	imageWidth = 480
	maximumPixelStrength = 255
	halfMaximumPixelStrength = 124	
	output = np.array(input_array, dtype = np.float32)
	a = output.shape[0]
	b = output.shape[1]
	output = np.multiply(output, maximumPixelStrength)
	while a < imageWidth:
		output = output.astype(np.float32)
		output = np.multiply(output, 1.0 / maximumPixelStrength)
		a *= 2
		b *= 2
		output = cv2.resize(output, (a, b))
		output = np.multiply(output, maximumPixelStrength)  
		output = np.rint(output)
		output = output.astype(np.uint8)
		retval, output = cv2.threshold(output, halfMaximumPixelStrength, maximumPixelStrength, cv2.THRESH_BINARY)
	cv2.imshow('Apriltag', output)
	cv2.waitKey(300)
	return
	
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
	for row in output:
		for element in row:
			print(element, end = ' ')
		print()
	return output

if __name__ == "__main__":
	mainFunction()	
	
