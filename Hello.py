# print("hello World")
# print(25+12)
# print("Bye")
# print("Nitesh")
# print("Kumar")
# print("Mandal")
# Hey this is a comment line 
#Author : Nitesh 
#100 days of code


# print("Hey" , 7 , 8 , sep="~" , end= "009\n")
# print("Nitesh")

#Data types 

x = 10        # int
y = 3.14      # float
z = 2 + 3j    # complex

name = "Nitesh"  #String
my_list = [1, 2, 3, "hello"]
student = {"name": "Nitesh", "age": 20} #Dictionary
is_valid = True # Boolean
x = None
s = {1, 2, 3} #set

# print("Data type of s is : " , type(s))
# print("Data type of student is : " , type(student))
# print("Data type of name is : " , type(name))
# print("Data type of is_valid is : " , type(is_valid))

#TypeCasting

# x = "100"
# y = int(x)
# print(y+50)

a = 10
b = float(a)
print(b)   # 10.0

num = 25
text = str(num)
# print(text + " is a number")

#Taking User input

# x = input("Enter first number : ")
# y = input("Enter Second number : ")
# print(int(x)+int(y))

#Strings 
#--> Strings are immutable

name = "Nitesh"
friend = "Rahul"
anotherfriend = 'Satyam'

apple = '''he said ,
Hi harry 
hey i am good
"I want to eat an apple 
'''
# print(apple)
# print(name[0])
# print(name[1])

# for char in name:
#     print(char)

#String Slicing 

names = "Nitesh,Subham"
# print(len(names))
# print(names[0:6]) #excludes last index --> including 0 but not 6
# print(names[0:-4]) #[0:len(names)-4]  0-9
# print(names[-3:-1])  #10-12


#String methods 

a = "Nitesh!!!!! !!!! !"
# print(a.upper())
# print(a.lower())
# print(a.rstrip("!"))
# print(a.replace("Nitesh" , "harry"))
# print(a.split())
# b = "introduction to python programming"
# print(b.capitalize())
# str1 = "Welcome to console!!"
# print(len(str1))
# print(len(str1.center(50)))
# print(a.count("Nitesh"))
# print(a.find("i"))
# str2 = "welcome00 "
# str3 = "Hey Nitesh"
# print(str2.isalpha())
# print(str3.isalnum())
# str4 = "   "
# print(str4.isspace())

#Else if statement 

# age = 25

# if age >= 18:
#     print("You can vote")
# else: 
#     print("You cannot vote")

# marks = 75

# if marks >= 90:
#     print("Grade A")
# elif marks >= 70:
#     print("Grade B") 
# elif marks >= 50:
#     print("Grade C") 

# else:
#     print("Fail")  


# num = 10

# if num > 0:
#     if num % 2 == 0:
#         print("Positive Even")
#     else:
#         print("Positive Odd")

# age = 20

# if age > 18 and age < 60:
#     print("Working age")

# if age < 18 or age > 60:
#     print("Not typical working age")

# num = 5
# id(num)  #address of num
# print(id(num))

# name = 'Nitesh'
# print(id(name))

# a = 10
# b = a
# print(id(a))
# print(id(b))
# if two variable have same data then they have same memeory location , python is memory efficient  


#Data types in python 
#None 
#Numeric  -- int(5) , float(2.5) , complex(6+9j) , bool(0,1)
#List --[1,2,3,4,5] , mutable 
#Tuple -- (1,2,3,4,5) , immutable 
#Set --{1,2,3,4,5}, unique values 
#String  -- "Nitesh"
#Range -- range(0,10) range of values 
#Dictonary -- {1:"Mango" , 2: "Apple"} Key value pairs 