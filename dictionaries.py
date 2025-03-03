student = {"name" : "Alice", "age": 16, 'grade': "A"}
print(student) # {'name': 'Alice', 'age': 16, 'grade': 'A'}
name = student.get('name',"No name") 
city = student.get('city', 'No city assigned') 
print(name) # 'Alice' --> because name exists
print(city) #'No city assigned' --> because city isn't a key in the Dictionary
student['age'] = 19 #change age to 19
print(student) #{'name': 'Alice', 'age': 19, 'grade': 'A'}
student['city'] = "Winnipeg" # creates a key-value pair
city = student.get('city', 'No city assigned') # Winnipeg
print(city) #Winnipeg --> because city now exists it outputs Winnipeg


#print(student)
#del student["grade"] # A
#print(student) 
# #{'name': 'Alice', 'age': 19, 'grade': 'A', 'city': 'Winnipeg'}

#print(student.values()) 
# #dict_values(['name', 'age', 'grade', 'city'])
#print(student.keys())
# #dict_keys(['Alice', 19, 'A', 'Winnipeg'])
#print(student.items())
# #dict_items([('name', 'Alice'), ('age', 19), ('grade', 'A'), ('city', 'Winnipeg')])

#for key in student.keys():
#    if key == "name":
#        print("Woohoo -- it's Alice!")
#    else:
#        print("nope")
# #output --> 
# #Alice
# #nope
# #nope