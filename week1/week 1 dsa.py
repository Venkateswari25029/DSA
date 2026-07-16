#Comparing number with zero
"""num=int(input("Enter the number:"))
if(num>0):
    print(f"{num} Greater than zero")
else:
    print(f"{num} Number less than zero")
"""
    
#if-elif-else condition
"""num=int(input("Enter the number:"))
if(num>0):
    print(f"{num} greater than zero")
elif(num>0):
    print(f"{num} less than zero")
else:
    print(f"{num} is zero")
"""
#Nested if statement
"""
num=int(input("Enter the number:"))
if(num>=0):
    if(num==0):
        print("It is equal to zero")
    else:
        print("it is positive")
else:
    print("Number is negative")
"""
#LOOP
#For loop
"""cars=["swift","Nano","bmw"]
for car in cars:
    print(car)
    print("------")
print("For loop ended")
"""
#For loop through string
"""str=(input("Enter the string:"))
for i in str:
    print(i)
"""
#Generate numbers from 1 to 10
"""for i in range(1,11):
    print(i)
"""
#With break and continue statement
"""for i in range(1,11):
    if(i==5):
        continue
    if(i==7):
        break
    
    print(i)
"""
#Nested for loop
"""cars=["maruthi","Nano"]
bikes=["tvs","ktm"]
for car in cars:
    for bike in bikes:
        print(bike)
    print(car)
print("******")
"""
#without using sequence items
"""for _ in range(0,3):
    print("Sahithi")
print("loop ended successfully")
"""

#While loop
#Generating numbers from 1 to 10
"""num=1
while num<=10:
    print(num)
    num=num+1
"""
#print the numbers until user enters 0
"""num=int(input("Enter the number:"))
while(num!=0):
    print(num)
    num=int(input("Enter the number:"))
print("Loop ended")
"""
#Pass statement
"""num=int(input("Enter the number:"))
if(num<4):
    pass
print("Hello")
"""
#List
# a list of three elements
"""ages = [19, 26, 29]
print(ages)
print(ages[0])
print(ages[:2])
"""
"""fruits=["apples","orange","mango"]
fruits.append("pineapple")
print(fruits)
"""
"""fruits=['apple', 'banana', 'orange']
print("Original List:", fruits) 
fruits.insert(2, 'cherry')
print("Updated List:", fruits)
"""
"""color=["red","green","yellow"]
color[0]="blue"
color[2]="purple"
print(color)
print(len(color))
color.clear()
print(color)
"""
























