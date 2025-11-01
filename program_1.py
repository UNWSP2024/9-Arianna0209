# Name Counter
# Author: Arianna Endres
# Date: 10/31/2025

# Assume a file containing a series of names (as strings) is named names.txt
# Write a program that displays the number of names that are stored in the file.

def count_file_lines():
    namefile = open('names.txt', 'r')
    name = namefile.readline()
    name_count = 0
    while name != '':
        name_count += 1
        name = namefile.readline()

    print(f'There are {name_count} names in the names.txt file')

    namefile.close()

# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()