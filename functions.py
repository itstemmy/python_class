# function--- a function is a block of code which only runs when it is called.
# you can pass data known as parameters into a function.
# in python a function is defined using the DEF keyword
# we have 2 types of functions i. user define function and ii. built-in function
# user define function: 
# def myname():
#     print("suleiman Muhammed Dexter")

# myname()

# arguement: information can be passed into function as arguement, arguement are specified after
# the function name inside the parenthesis
# def fullname (fname,lname,sname):
#     return fname + " "+lname+" "+sname

# print(fullname("Sulaiman","Ade","Muhammed"))

# def sum_number(x,y):
#     return x+y

# num1 = 12
# num2 = 13
# print(sum_number(num1,num2))

# def profile(name, school, age):
#     return "my name is"+" "+name+" "+"i am from "+school+" "+"i am "+str(age)+" "+"years old"

# print(profile(age=20,school="unilorin",name="sulaiman"))

# def check(score):
#     grade =""
#     if score >=75:
#         grade = "A"
#     elif score <=74 and score >=60:
#         grade = "B"
#     elif score <=59 and score >=50:
#         grade = "C"
#     else:
#        grade = "F"
#     return gradescore = ""
# while score !=-1:
#     score = eval(input("enter your score : "))
#     if score == -1:
#         break
   # print(check(score))


# arbitrary arguement allows us to add numerous data i.e
# def myname(*name):
#     return name
# print(myname("Sulaiman","Ade","Ibrahim","sharon"))


# arbirary keyword arguement
# this function returns a dictionary
# def myname(**name):
#     return name
# name = myname(fname="Sulaiman",sname="Muhammed",age=20,course="chem")
# print(name)

# for key,value in name.items():
#     print(key,value)

# def num(number=0):
#     print(number)

# def check(score):
#     grade =""
#     if score >=75:
#         grade = "A"
#     elif score <=74 and score >=60:
#         grade = "B"
#     elif score <=59 and score >=50:
#         grade = "C"
#     else:
#        grade = "F"
#     return grade






#create a function that takes in a list and printout all the list element using
#for loop


#lambda function----its a small anonimous function can take any number of arguement but can 
#only have one expression---- 
#lambda args : expression
#x = lambda y,a :a+y
#print(x(12,13))

x = lambda y: max(y)
lst = [1,3,4,5,6,7,98]
print(x(lst))