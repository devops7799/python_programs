import os
folders = input("Please enter folder names separated by spaces: ")
#print(folders.split())
for folder in folders.split():
	#print (folder)
	try:
		print(os.listdir(folder))
	except FileNotFoundError:
		print(f"{folder} does not exist")
	except PermissionError:
    print(f"{folder} is not accessible")
