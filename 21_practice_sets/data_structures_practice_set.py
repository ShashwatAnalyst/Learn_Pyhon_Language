# 1. create a list fruits = ['apple','banana','orange'] 
# print first fruit
# print length of list fruits 
# replace banana with cherry

fruits = ['apple','banana','orange']

print(fruits[0])
print(len(fruits))
fruits[1] = "cherry"
print(fruits)

# 2. create a list of number from 1 to 10 
# print first 3 numbers using slicing 
# print lanst 3 numbers using slicing

numbers = [i for i in range(1,11)]

print(numbers[0:3])
print(numbers[-3:])

#3. create a list [5,2,9,1,7]
# sort the list in ascending order
# append the number 10 to the list
# remove number 2 from this list

list1 = [5,2,9,1,7]

list1.sort()
print(list1)

list1.append(10)
print(list1)

list1.remove(2)
print(list1)

# 4. create a tuple coordinate = (10,20) and print both elements
# modify the tuple coordinate[0] = 50 - note what happens
# convert the tuple to list change its first element to 50 , and convert it back to tuple

coordinate = (10,20)
# coordinate[0] = 50 TypeError: 'tuple' object does not support item assignment
coordinate = list(coordinate)
coordinate[0] = 50
coordinate = tuple(coordinate)
print(coordinate)

# 5. create a set  my_set = {1,2,3,3,4} , what happens to duplicate 3 ? 
# add 5 to the set , remove 2, check if 4 is in the set
# create 2 sets 
# a = {1,2,3}
# b = {3,4,5}
# find there union , intersection , difference a-b

my_set = {1,2,3,3,4}
print(my_set)

my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)

a = {1,2,3}
b = {3,4,5}

union = a.union(b)
print(union)

intersection = a.intersection(b)
print(intersection)

difference = a.difference(b)
print(difference)

# 6. create a dictionary student = { "name" : "john" , "age" : 20 , "grade" : "A"}
# print value of "name"
# change "grade" to "A+"
# Add a new key "city" with value "Delhi"

student = { "name" : "john" , "age" : 20 , "grade" : "A"}

print(student["name"])

student["grade"] = "A+"
print(student)

student["city"] = "Delhi"
print(student)

# 7. create a dict of 3 friends with their ph no. use .keys, .values , .items

friends = {"tushar": 8289198279 , "jay" : 7862839292 , "yash" : 8273828973}

print(friends.keys())
print(friends.values())
print(friends.items())

# 9. write a program that takes a list of number and removes all the duplicates using a set

def drop_duplicates(l):
    s = set(l)
    l1 = list(s)
    return l1

l = [1,2,3,4,4,5]
print(drop_duplicates(l))

# 10. write a program that merges two dictionaries to one 

def merge(dict1,dict2):
    dict3 = dict1.copy()
    return dict3.update(dict2)
 
dict1 = {"name" : "lisa","cgpa":9.5}
dict2 = {"city" : "delhi","gender":"female"}

dict3 = merge(dict1,dict2)
print(dict3)

#11. Find the product with the highest price.

products = {"iphone 10" : 50000 , "iphone 11" : 60000 , "iphone 12" : 80000}

max_prod = max(products.values())

print(list(products.keys())[list(products.values()).index(max_prod)])
