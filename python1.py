name = "Steven"
print("Hello " + name) 
print("Hello", name)

name = input("Enter your name here: ")
print("Hello", name)
tester = 0

while tester==0:
    hours = input(f"How many hours did you work {name}? ")
    try:
        hours = float(hours)
        tester=1
    except:
        print("Not numbers")
        continue
    
    
print(hours + hours)