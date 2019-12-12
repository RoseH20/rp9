#First Program
#Scenario: a program that calculates the weight of an object that has a mass of 7.26 kg
#SOLUTION: Weight is mass multiplied by gravity (W = mg).
#Let's program it!
#First step - initialize variables by keeping in mind what value will remain constant throuhout
#a program and what will not

constant_values = (9.8)     #since gravity is constant at every mass
mass = 7.26
weight = constant_values * mass
unit_of_weight = "Newtons"
print(weight, unit_of_weight)
