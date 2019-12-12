#Exercises
#1 - write a program that compares values of 'a' and 'b'
#and inverts the result (fals becomes true and true becomes false)
#'a' = 3 and 'b' = 2
a = 3
b = 2
print(not(a == b))

#2- write a program that checks whether "Josh" is on the list and also checks
#whether "Marie" is not on the list
#list of members is "Josh, Adam, Ervin"
list = ["Josh", "Adam", "Ervin"]
josh = "Josh"
marie = "Marie"
print(josh in list)
print(marie not in list)
