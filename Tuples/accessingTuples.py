#Real world Example of Tuple Indexing: Student Information

#Create tuple with a student's information
#Format: (name, age, grade, courses) # courses will be a nested Tuple
student = ("Sue Baker", 19, "Grade 12", ("Computer Science", "Math", "Physics"))

#Access each elements using positive indexing 
print("Student Name:", student[0]) #first element -- "Sue Baker"
print(f"Student Age: {student[1]}") #second element -- 19 - f string access

#Accessing nested Tuple items
print(f"First Course: {student[3][0]}") # Computer Science

#Negative indexing examples
print(f"Grade Level: {student[-2]}") # Grade 12
print(f"Last Course: {student[3][-1]}") # Physics

#Practical use -- Breaking down student information
name = student[0] 
age = student[1]
gradeLevel = student[2]
courses = student[3]

# \n - gives us a line space -- or carriage return
print("\nDetailed Student Info:")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Grade Level: {gradeLevel}")
print(f"Courses: {', '.join(courses)}")


# {', '.join(courses)}
# here we take each tuple element and join them into one sentence
# we separate them with a comma and space so that it looks like this:
# Computer Science, Math, Physics