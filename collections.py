# List are one of 4 built-in data types in python used to store
# collections of data in python. others are tupple, set, dictionary all with different
# quality and usage.
# list are created with [squre bracket]
# i.e list = ["rice","beans","garri","semo"]
# num = [1,2,3,4,5,6]
# list items are ordered changeable and allow duplicate value.
# list items are indexed. the fist item has [0] while the second item has [1] and so on

#lst = ["rice", "beans","yam","garri","semo"]
# num = [1,2,3,4,5,6]
# print(lst)
#lst[0] ="poundo"
#print(lst)
#lst1 = ['mang',123,True,lst]
#print(lst1[3])
#print(lst1[0])
#lst2 = list(("john","Balo","dexter","Bolu","Ade","precious"))

# negative index -1 is the last element. 
#lst2[starting point: end point exlusive]
#print(lst2[ 1:])
#print(lst2[-5: -1 ])
#if "john" in lst2:
#   print("john is present ")
#lst2[1:5] = ["Tope","Maryam","Emmanuel","Aarif"]
# print(lst2)

# append() adding of new data

#lst2.append("suleiman")
#lst2.append("muhammed")
# print(lst2)

# insert(index, data) uses
#lst2.insert(0,"sharon")
#lst2.extend(lst)
#print(lst2)

#remove data
#remove()
#lst2.remove("suleiman")
#print(lst2)
#lst2.clear()
# print(lst2)


# #how to use pop() it is used to remove an element from the list. when the pop function is empty,
# #it remove the last element from the list. we can specify the index of element to be deleted.
# lst2.pop()
# print(lst2)
# #to specify the element to remove
# lst2.pop(2)
# print(lst2)


# #del() this is used to remove an element from the group

# del lst2[5]
# print(lst2)

#copy()

#lst3 = lst2.copy()
#print(lst3) or

# lst3 = list(lst2)
# print(lst3)
# #to get the lenght of a list
# len_lis = len(lst2)
# print(len_lis)

#extend function only works on collection.e.g dictionary,set,list and tupple

# fruits = list(("mango","orange","banana","apple","kiwi"))
# for fruit in fruits: 
#     print(fruit)
# #looping thru list using the length
# len_fruits = len(fruits)
# for index in range(len_fruits): 
#     print(index)

# #using while loop 
#len_fruits = len(fruits)
#init = 0  #(initial value)
#for index in range(len_fruits): 
 #   print(fruits[index])
#while init < len_fruits:
 #   print(fruits[init])
 #   init +=1
#to specify
# init = 1
# while init < len_fruits:
#     print(fruits[init])
#     init +=1

#numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
#print out the even numers from the above list using for loop 
#for index in range(len(numbers)):
#    if numbers[index]%2 ==0:
#        print(numbers[index])
# for odd numbers
# for index in range(len(numbers)): 
#     if numbers[index]%2 ==1:
#         print(numbers [index])

# num = []
# for i in range(1,15): 
#     num.append(i)
# print(num)

# #list comprehension

# num2 = [i for i in range(1,14)]
# print(num2)
# #to print even number
# num2 = [i for i in range(1,30) if i%2==0]
# print(num2)

# scores = [50,45,60,40,12]
# total_score = 0
# for score in scores:
#     total_score = total_score +score
# print(total_score)
# #to get minimum or maximum
# max_no = max(scores)
# min_no = min(scores)
# print(max(scores))
#to get mean/average
#print(total_score/len(scores))

#li = [23,40,45,12,26,29,89,100]
#li2 = ['John','Precious','Ayat','Salman']
#using a for loop append li2 values to li list
#for x in li2:
    #li.append(x)
#print(li)


# tupple; tupple are used to store multiple item in a single variable.tupple is one of 4 built-in data types in python used 
# to store collections of data. a tupple is a collection data which is ordered and unchangeable and allow
# duplicate values.
# it is declared with a round bracket() e.g
#name = ("bola","maryam","dexter",12)
#to get the lenght
#print(name[:3])


#unpacking a tupple; this is a way of extracting the values of a tuppleback into variables
# profile = ("Muhammed",20,"engineering")
# (name, age, course) = profile
# print(name)
# print(age)
# print(course)
# create a tupple with the names of fruits using for loop printout the fruits
# on a new line
# fruits = ("apple","orange","mango","banana","cherry")
# for items in fruits:
#     print(items)
# to multiply value
# fruit = (4,6)
# print(fruit*4)




# range of indexes
#this is to specify the starting point and the end point
#dictionary; dictionarries are used to store data value in key: valuepairs
#a dictionary is a collection which is ordered changeable and do not allow duplicate.
#dict = {'key:value'}
profile = {"name":"sulyman","lastname":"Toha","age":20,"occupation":"software Dev"}
#accessing items in dictionary --- you can access the items of a dictionary by refering to its key
#name inside a square bracket
#print(profile["name"])
#print("my name is "+profile['name']+" "+profile["lastname"])

#using get() method
#print("my name is "+profile.get('name')+" "+profile.get('lastname'))
#profile_keys = profile.keys()
#print(profile_keys)
#profile_values = profile.value()
#print(profile_values)

#changing of items in dictionary--- u can change the value of a specific
#item by refering to its key name
# profile['name'] = 'Abbass'
#print(profile)
#update() it is also used to make changes in the value of the keys
#profile.update({"name":'Abbass'})
#print(profile)




#carts = {"Rice":1200,"Beans":3000,"milk":5000,"Noodles":3700}
#for cart in carts.values(): #for only value
#print(cart)
#for key,value in carts.items(): #for both value and key
 #   print(key, value)
   

#prod = carts.copy() #to copy from one dictionary to the other
#print(prod) #or

#prod = dict(carts)
#print(prod)

# nested dictionaries---- that means having a dictionary inside dictionary.
profile = {
    "dexter": {"name":"Sulaiman","age":20,"occupation":"software dev"},
    "segcode":{"name":"Segun","age":21,"occupation":"ml Engr"}
}
#print(profile["dexter"]) #or
#print(profile["dexter"].get("name"))
#print(profile["segcode"].get("name"))

# SET 