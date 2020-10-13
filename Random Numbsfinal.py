#Tyler Prentiss
#October 10, 2020
#Programming Exercise 6-7&8
#Random Number Machine

# import the random module
import random
from statistics import mean

# define the main function

def main():

#open a file for writing and assign it to the variable random_numbers.
    random_numbers = open('ran_numbers.txt', 'w')

#get the number of random numbers to be generated
    qty_numbers = int(input('How many random numbers should be written to the file? '))

    print('Your list of random numbers are: ')
    rlist = []
#create a loop to generate the random numbers in the quantity specified
    for count in range (qty_numbers):
        number = random.randint(1,500)
    rlist.append(number)
#print the list of random numbers
    print(number)
 
    mytotal = sum(rlist)
    myaverage = mean(rlist)

#convert the numbers to a string and write them to the file
random_numbers.write(str(number)+ '\n')
   
#close the file
random_numbers.close()

#tell the user that the numbers have been written to the file name.
print('Your list of random numbers have been written to the file named')
print('ran_numbers.txt')

#call the main function

main()
