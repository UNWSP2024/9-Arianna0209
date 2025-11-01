# Total of File Numbers
# Author: Arianna Endres
# Date: 10/31/2025

# Assume a file containing a series of integers is named numbers.txt and exists on the computer's disk.
# Write a program that reads all of the numbers stored in the file and calculates their total.  

# The program should handle the following exceptions: 

# It should handle any IOError exceptions that are raised.
# It should handle any ValueError exceptions that are raised when the items that are read from the file 
# are converted to a number.

def sum_numbers_from_file():

    numbers_file = open('numbers.txt', 'r')

    try:
        total = 0
        for line in numbers_file:
            number = int(line.rstrip('\n'))
            total += number
        print(f'The total of the numbers in the numbers.txt file is {total}')

    except IOError:
        print('An error occurred trying to read the file.')

    except ValueError:
        print('A non-numeric value was found in the file.')

    except:
        print('An unknown error occurred.')


# You don't need to change anything below this line:
if __name__ == '__main__':
    sum_numbers_from_file()