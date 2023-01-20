#primitive data types
#int - whole numbers
#string - anything in quotes ""
#boolean - true or false
#float - number with decimal

#if statements
#if (boolean expression)
#do some code

number_as_string = input("Give me a number: ")
number = int(number_as_string)

if (number > 10):
    #do some code
    print("Number is greater than 10 :)")
else:
    #do some more code
    print("Number is NOT greater than 10 :(")


#if-elif-else branch

#python has built in libraries - random number is one
import random
#randint() just grabs a random number 
random_number = random.randint(1, 30)
print("Random number: " + str(random_number))

#because these are elif's, it only 
if random_number < 10:
    print("Number is less than 10")
elif random_number < 20:
    print("Number is less than 20")
elif random_number < 25:
    print("here")
else:
    print("Number is 20 or greater")



#LIST
#data structures - something that you hold data in (int, floats, boolean, string)
#most common is list
items = []
items.append(0)
items.append("lucas")
items.append(True)
items.append(6.9)

number = 200
other_number = 40 
other_other_number = 5
numbers = []
numbers.append(number)
numbers.append(other_number)
numbers.append(other_other_number)
#print(numbers)

# numbers.sort(reverse=True)
# numbers.sort()
# print(numbers)


#looping - iterating, or in any words going one by one, through a data structure
#while loop
#while (boolean expression) 
#do some code
counter = 1
while(counter < 10):
    print(str(counter))
    counter = counter + 1

#loop over a data structure
items = []
items.append("milk")
items.append("eggs")
items.append("bread")
items.append("water")
items.append("bacon")
#print(items)
first_item = items[0]
second_item = items[1]

#looping by element
#for loop - for each loop
for item in items:
    print(item)





# looping over a list by indexing
# counter variable to iterate over the list (all lists start at 0)
counter = 0

#length of the list (number of items)
length_of_list = len(items)

#loop to go over the list
while (counter < length_of_list):
    #item at each index
    item = items[counter]
    print("Item is: " + item)
    counter = counter + 1

