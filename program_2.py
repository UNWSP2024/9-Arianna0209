# Random Number Writer
# Author: Arianna Endres
# Date: 10/31/2025

# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).

import random

numberfile = open('randomnumbers.txt', 'w')

def numberfile_writer(numberfile):
    while True:
        try:
            number_of_numbers = int(input('How many random numbers (up to 1000) would you '
                                          'like written on the randomnumbers.txt file? '))
            if number_of_numbers <= 1000:
                for number in range(number_of_numbers):
                    numberfile.write(str(random.randint(1, 500)) + '\n')
                return number_of_numbers

            elif number_of_numbers == 1111:
                print('You have chosen to end the program.')
                return None

            elif number_of_numbers > 1111:
                print('Please enter a number between 1 and 1000. Please try again '
                      'or type 1111 to exit.')

        except ValueError:
            print('You must enter an integer. Please try again or type 1111 to exit.')

        except:
            print('Something went wrong. Please try again or type 1111 to exit.')

def main():
    result = numberfile_writer(numberfile)
    if result is not None:
        print(f'{result} random numbers were written on the randomnumbers.txt file.')
    numberfile.close()

if __name__ == '__main__':
    main()