import random

def trimLinesInFile(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Define the maximum number of lines to keep 
    maximumLines = 4000

    # This will extract the name elements in lines list from lines[0] to lines[maximumLines-1]
    trimmed_lines = lines[:maximumLines]

    with open(file_path, 'w') as file:
        file.writelines(trimmed_lines)

def numOfLines(file_path): 
    with open(file_path, 'r') as file:
        # Read all lines and calculate the total number of lines
        lines = len(file.readlines())     
        print('Total Number of lines in', file.name, ':', lines)


def generateFullNames(filePath1, filePath2, filePath3):
    # Initialize an empty list to store full names
    fullNames = []

    # Define the number of entries to generate
    entries = 4000

    with open(filePath1, 'r') as file:
        firstNames = [line.strip() for line in file.readlines()] #strip() method is used to remove any leading or trailing whitespaces

    with open(filePath2, 'r') as file:
        lastNames = [line.strip() for line in file.readlines()]#strip() method is used to remove any leading or trailing whitespaces

    # Generate full names by randomly combining first and last names and save in a list called fullName
    # random.choice() function will randomly select a name from the list.
    # formatted string literal will evaluate {random.choice(firstNames)} and {random.choice(lastNames)} and replace the curly brackets with their values resulting a full name string.
    # For each iteration (_ in range(entries)), a random full name is generated and added to the fullNames list.
    fullNames = [f"{random.choice(firstNames)} {random.choice(lastNames)}" for _ in range(entries)]
    return fullNames

def writeToFile(nameList, filePath):
    with open(filePath, 'w') as file:
        for name in nameList:
            file.write(name + '\n')

def getLongestName(file_path):
    with open(file_path, 'r') as file:
        fullNames = file.readlines()
    
    # Define the number of entries to generate
    entries = 4000

    # Find the longest full name among the generated names
    longestFullName = ""
    for i in range(entries):
        if len(fullNames[i]) > len(longestFullName):
            longestFullName = fullNames[i]

    # Print the longest full name
    print("Longest Full Name is", longestFullName)



firstNamesPath = 'firstNames.txt'
lastNamesPath = 'lastNames.txt'
fullNamesPath = 'FullNames.txt'
trimLinesInFile(firstNamesPath)
trimLinesInFile(lastNamesPath)
numOfLines(firstNamesPath)
numOfLines(lastNamesPath)
fullNamesList = generateFullNames(firstNamesPath,lastNamesPath,fullNamesPath)
writeToFile(fullNamesList,fullNamesPath)
getLongestName(fullNamesPath)
