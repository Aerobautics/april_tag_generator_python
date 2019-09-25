#!/usr/bin/python
import numpy as np
import cv2

def mainFunction():
	maximumValue = 68719476735
	mean = maximumValue // 2
	choice = 12
	while choice:
		displayMenu()
		choice_string = input("Enter choice: ")
		choice = int(choice_string)
		if choice == 0:	
			print(choice)
		elif choice == 1:
			print(choice)
			temporary = generateArray(mean)
			temporary = generateImageValues(temporary)
			generateImage(temporary)
		elif choice == 2:
			print(choice)
		elif choice == 3:
			print(choice)
		elif choice == 4:
			print(choice)
		elif choice == 5:
			print(choice)
		elif choice == 6:
			print(choice)
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
	output = np.array(input_array, dtype = np.float32)
	output = cv2.resize(output, (480, 480))
	cv2.imshow('Apriltag', output)
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
			#print(temporary % divisor)
			if temporary % divisor > 0:
				output[i][j] = False
			else:
				output[i][j] = True
			temporary = temporary // divisor
	for row in output:
		for element in row:
			print(element, end = ' ')
		print()
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
	
