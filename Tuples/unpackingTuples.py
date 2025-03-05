# Real World examples of tuple unpacking: Multiple Use Cases

#1 - Basic Student Information Unpacking
studentInfo = ("Sue Barker", 20, "Computer Science", 3.85)
name, age, major, gpa = studentInfo
print("Student Profile:")
print(f"Name: {name}") # Name: Sue Barker
print(f"Age: {age}") # Age: 20
print(f"Major: {major}") # Major: Computer Science
print(f"GPA: {gpa}") # GPA: 3.85

#2 - Geolocation Coordinates Unpacking
locationData = (40.7128, -74.0060, 10.5, 0.5)
lat, lon, alt, accuracy = locationData
print("\nLocation Details:")
print(f"Latitude: {lat}") # Latitude: 40.7128
print(f"Longitude: {lon}") # Longitude: -74.0060
print(f"Altitude: {alt}") # Altitude: 10.5
print(f"Accuracy: {accuracy}") # Accuracy: 0.5

# 3 - Swapping Variables
#Dome how tuple unpacking makes variable swapping easy
a, b = 10, 20
print("\nBefor Swapping:")
print(f"a = {a}, b = {b}") # a = 10, b = 20

#Swap Variables using tuple unpacking
a, b = b, a
print("After Swapping")
print(f"a = {a}, b = {b}") # a = 20, b = 10

# 4 - Function returning multiple values
def getProductDetails():
    """
    Simulate getting product info
    Returns a tuple with product details
    """

    return ("Wireless Headphones", 129.99, 50, "Electronics")

#Unpack returned tuple directly
productName, price, stock, category = getProductDetails()
print("\nProduct Information:")
print(f"Name: {productName}") # Name: Wireless Headphones
print(f"Price: ${price}") # Price: $129.99
print(f"Stock: {stock} units") # Stock: 50 units
print(f"Category: {category}") # Category: Electronics

# 5 - Partial Unpackign with Star Operator -- *
# Demo unpacking with variable number of elements
techStack = ("Python", "JavaScript", "React", "Node.js", "MongoDB")
primaryLanguage, *secondaryLanguages = techStack
print("\nTech Stack:")
print(f"Primary Language: {primaryLanguage}") # Python
print(f"Secondary Language: {secondaryLanguages}") # ['JavaScript', 'React', 'Node.js', 'MongoDB']

# Another Star operator example
first, *middle, last = (1, 2, 3, 4, 5)
print("\nStar Operator Example:")
print(f"First: {first}") # First: 1
print(f"Middle: {middle}") # Middle: [2, 3, 4]
print(f"Last: {last}") # Last: 5

# 6 - Nested Tuple Unpacking
employee = ("John Doe", 35, ("Software Engineer", "Backend"))
name, age, (jobTitle, department) = employee
print("\nEmployee Details:")
print(f"Name: {name}") # Name: John Doe
print(f"Age: {age}") # Age: 35
print(f"Job Title: {jobTitle}") # Job Title: Software Engineer
print(f"Department: {department}") # Department: Backend

#7 - Ignoring Some Values with Underscore  _
contactInfo = ("John", "Doe", "867-5309", "john@example.com")
firstName, lastName, *_ = contactInfo
print("\nPartial Contact Info:")
print(f"First Name: {firstName}") # First Name: John
print(f"Last Name: {lastName}") # Last Name: Doe
# skips the phone and email here