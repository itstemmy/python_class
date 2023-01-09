# +, -,*,/,%,
#x = 10
#y = 10
#print(x + y)

#Augmented or compound assignment operators
#addition
# x = 10
# x = x + 1
#x += 2 (this is augmented operator bcos it assign the value of x)
#print(x)
 
 #subtraction
# y = 10
 # y = y - 1
 #y -= 1 (augmented operator)
 #print (y) 
 #(i.e y = 9)

 #division
#a = 30
#  a = a / 2
# a /= 2
# print(a)

#multiplication

# x = 30
# x *= 5
# print(x)

# comparison operators: it can be used to compare the value of operands
# == -- equality operator
# != -- not equality operator
# > -- gt
# < -- lt 
# >= --gte
# <= --lte

# x = 3
# y = 3
# print(x == y)

# a = 10
# b = 20
# print(a != b)

# a = 55
# c = 20 
# print(a > c)

# x = 55
# c = 20
# print(x < c)

# logical operators

# this can be used to compare multiple conditions
# and -- it will return true if both conditions compared is true 
# or-- this will return true if either of the condition compared / tested is true
# not--- this will return the inverse of the condition tested
#strings
# strings() this a textual data surrounded with quotes (double or single)
# it is a sequence of character. strings are immutable (they cannot be modified or changed)
# strings like other data type also employ zero indexing i.e you start counting from zero

#example
# data = "python programming"
# print(data)

# how to get the lenght of a string
# the length of a string is the number of character in a string
# len()-- this caan be used to get the length of a string
#data = "python programming"
# print(len(data))


#accessing individual character in a string using indexing
#individual characters in a string can be accessed using bracket [] notation
#print(data[0])
#print(data[17])
# print(data[8])

# slicing; this print multiple character
# e.g to print python it is
#print(data[0:6])
#to print pyt it is
#print(data[0:3])
 
# print(data[7:18])
#print(data[-11:-4])
# reversing a string
# name = input('enter name: ')
# print(name[::-1])

#string methods-- are function that are specific to python strings
#methods are functions that is accessible using the dot notation.
#data = "python programming"
#print(data.capitalize()) this is used to capitalize the first word 
#print(data.title()) this is used in each word in a sentence 
#print(data.find("p")) this locate the position of the word

#print(data.find("z")) this shows -1 bcos its not in data
#print(data.upper()) this change the word to uppercase
#print(data.lower()) to change to lower
#print(data.endswith("g")) it return word in boolean i.e true or false
#print(data.startswith("p"))  
#print(data.count("p")) it counts
#print(data.isupper()) it return false bcos its not in uppercase
#print(data.islower()) it return true bcos its in lowercase
#print(data.casefold()) it returns the original word

#print(data.format())
#using formatted function
# age = 30
# result = "i am {} years old"
# print(result.format(age))

#conditional statement : this tells a program to execute an action depending on whether the condition is true or false.
#it is often refer to as if-else statement.
# if statement tells a program to execute an action if the condition stated is true.
# else statement tells a program to execute an action if the condition stated in the if block is false.
# elif statement is used in a chained if statement when u are testing multiple conditions
# we make use of our logical and comparison operators here
  

# write a python program that checks the stenght of a password. if the password is less than 6 characters or it is greater than 12 characters, it should reject
# it should reject the user otherwise( it is not less than 6 or greater than 12) 
# it should accept the user
#correction
# password = input("enter your password: ")
# password_lenght = len(password)
# if password_lenght <6: or password_lenght >12:
#     print("password too short or too long")
#     else:
#         print('password correct')






# password = input("password: ")
# if len(password) <6:
#      print("password is not strong enough")
# elif len(password) >12: 
#      print("password should not be more than twelve characters")
# else: 
#     print("accepted")

#write a python program that assigns class of degree to students based on their GPA

GPA =float(input('enter your GPA: '))
if GPA >=4.50 and GPA <=5.00:
    print('first class')
elif GPA >=3.50 and GPA <=4.49:
    print('second class')
elif GPA >=3.49 and GPA <=2.50:
    print('third class')
elif GPA >=2.49 and GPA <=1.50:
    print('pass')
elif GPA <1.49:
    print('fail')
