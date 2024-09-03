# Create a Python script that displays the total number of items (both files and directories) present in the specified directory. 

# import os module
import os

# take the specified directory as input
dirPath = input("Enter your specified directory path: ")

# get list of files in directory
fileLists = os.listdir(dirPath)

# count the number of files in the specified directory
length = (len(fileLists))

# Print number of files to user
print(f"There are", length, "files in path:", dirPath)
