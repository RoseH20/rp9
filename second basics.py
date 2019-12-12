#Operators and Operands
#double == is a comparison operator
my_var = "I am some value in a string"
print(my_var == "I am some value in a string")
#output "True" as the left hand side and right hand side are the same

#GREATER THAN (>) OPERATOR
#used to check if the value is greater than some other value
my_var = 3.142
print(my_var > 3)

#GREATER THAN >= OPERATOR
my_var = 9.8
print(my_var >= 10)

#LESS THAN < OP
numeric_val = 999
print(numeric_val < 999)

#LESS THAN <= EQUALS TO
numeric_val = 665
print(numeric_val <= 665)

#NOT EQUAL OPERATOR !=
#! refers to NOT
str = "My name is Josh"
print(str != "My name is josh")
#lower j makes the non equal to statement true

#ARITHMETIC OPERATORS
#addition, subtraction, division, multiplication

#LOGICAL OPERATORS
#used in Conditional statements
#AND, OR , NOT
#if the return type is True, the block of code will run, False - it will not run
print(4 == 4 and 5 == 5)    #both conditions are true
print(4 == 4 or 6 == 5)     #one condition is true
print (not(1 ==4 and 5 == 5))   #brackets return false, and "not" makes it true
