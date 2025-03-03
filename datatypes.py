# when we declare a variable there is no need to say the type
#integer values -- whole numbers
num1 = 10
num2 = -5 # can be a positive or negative number
result = num1 + num2  #output -- 5
print(result)

#float values --> decimal numbers
float1 = 3.14 
float2 = -0.5 #can be negative as well
result = float1 + float2 #output -- 2.64
print(result) # result can change data types --> was an integer, now a float

#strings --> can use "" or ''
greeting = "Hello"
name = 'Alice'
message = greeting + ", " + name + "!"
print(message) #output -- Hello, Alice!

#Boolean values -- True or False
isSunny = True #it is case sensitive -- has to be capital T
isRaining = False 

#Comparison Operators
x = 5
y = 10
print(x == y) #False - 5 isn't equal to 10
print(x < y) #True -- 5 is smaller than 10
print(x >= y) #False -- 5 is smaller than 10

print(x < y and x != y) #True
# both 5 < 10 AND 5 != 10 -- both are true

print(x > y or x == y) # False
# 5>10 --> false OR 5 == 10 --> false - both false

print(x > y or x != y) #True
#5 > 10 --> false OR 5 != 10 --> true -- One is true. 

print(not(x==y)) #True
# 5 == 10 -- not says this is not true -- or 5 != 10

#list - ordered collection - changeable
numbers = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears"]
mixedList = [10, 'Python', True, "JavaScript"]

#Dictionaries -- unordered list - key:value pairing. 
student = {'name': 'Alice', 'age': 16, 'grade': 'A'}