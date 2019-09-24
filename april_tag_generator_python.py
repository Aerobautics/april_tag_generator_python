#!/usr/bin/python

def mainFunction():
	displayMenu()
	choice_string = input("Enter choice: ")
	choice = int(choice_string)
	if choice == 0:	
		print(choice)
	elif choice == 1:
		print(choice)
		generateArray(15439)
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
	
	
def displayMenu():
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
	
def generateImage():
	print("generateImage()")
	
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
		for j in range (len(output[i])):
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

if __name__ == "__main__":
	mainFunction()	
	
