# number = 10
# number2 = 0
# while number2<number:
#     print(number2)

# number = 10
# number2 = 0
# while number2<10:
#     print(number2)
#     if number2==9:
#         break
#     number2 +=1

# number = 10
# number2 = 2
# while number2<10:
#     print(number2)
#     if number2==9:
#         break
#     number2 +=3

#     continue
# i = 1
# while i<20:
#     i +=1
    
#     if i==10:
#         continue
#     print(i)

# num = 1
# while num <20:
#     num +=1
#     if num%2==0:
#         continue
#     print(num)
# else:
#     print("the condition is now false")

 #write a sript to print out numbers that are divisible by 5 within the range of 1 and 40
# number = 5
# number2 = 40
# while number <40:
#     number +=1
#     if number%5 ==0:
#         continue
#     print(number)
# else:
#     print("negative")

# msg = ""
# while msg != "quit":
#     msg = input("enter your message ")
#     print(msg)
 
#for loop is used to iterate over a sequence i.e tupple, dictionary, list, set
# for i in range(1,10):
#     if i==5:
#         continue
#     print(i)

# name = "international"
# count = 0
# for i in name: 
#     if i=="n":
#         count +=1
# print("the number n is :" + str(count))

#write a program that uses a while loop to read through a string and print the character of the string one by one on separate line



#write a program that allows a user to enter a number of test scores, the user indicate they are done by entering a -1

# score =""
# grade =""
# while score != -1:
#     score = eval(input("enter your score"))
#     if score >= 75: 
#         grade = "A"
#     elif score <=74  and score >=60:
#         grade = "B"
#     elif score <=59 and score >=50:
#         grade ="C"
#     else:
#         grade = "F"
#     print(grade)


# write a program that repeatedly asks the user to enter product name and prices.
# store all of these in a dictionary whose keys are the product names and whose values are 
# the prices. when the user is done entering product and prices, allow them to
# repeatedly enter a product name and print the corresponding price or a message if the
# product is not in the dictionary.

product = ""
price = 0
cart={}
while product !="quit":
    product = input("enter product name: ")
    if product == "quit":
        break
    price = eval(input("enter product price "))
    cart[product] = price
print(cart)
    #print(product)
    #print(price)
while product !="end":
    product = input("enter product name:")
    if product == "end":
        break
    if product in cart:
        print(cart[product])
    else:
        print("product not available")
    

    

