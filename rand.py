# #random number generation and file handling
# #python comes with a module called random that allows us to use random numbers
# #in our programs.
# #import random
# from random import randint

# num = 0

# while num !=-1:
#     ran = randint(0,200)
#     num = eval(input("guess a number"))
#     if num == -1:
#         break
#     if num ==ran:
#         print("correct")
#     else:
#         print("Try again the number is : "+str(ran))


x = open("name.txt" )
#print(x.read())
#print(x.readline())

#using for loop

#for name in x:
#    print(name)
#x.close() # to close the file after execution

# x = open("name.txt", "a") # to add to existing file using append
# x.write("Tunde\n")
# x.write("Bolaji\n")
# x.write("Bisola\n")
# x.close()


# x = open("name.txt", "w") # to overwrite the existing file
# x.write("Tunde\n") \n for the name to appear on a new line
# x.write("Bolaji\n")
# x.write("Bisola\n")
# x.close()


# to delete a File
# import os
# os.remove(filename.text)
# print("file deleted")

