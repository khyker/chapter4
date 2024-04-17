'''
Katellyn Hyker
Chapter 4 Project 8
Write a script that prompts the user for the names of two text files.
Input the contents of the first file and write it to the second file

'''
inputFile = input("Enter the input text file name(ex: text.txt): ")
outputFile = input("Enter the output text file name(ex: text.txt): ")

with open(inputFile, 'r') as reader, open(outputFile, "w") as writer:
        for line in reader:
            fields = line.strip().split()
            writer.write(",".join(fields)+"\n")