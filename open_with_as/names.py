with open("names.txt", 'w') as file:
	file.write('documents, downloads, programms')

with open('names.txt', 'r') as file:
	print(file.read())


