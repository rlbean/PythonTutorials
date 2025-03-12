# Try-Except with specific error messages
try:
    #Get user input
    num1 = int(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
# user enters a string value instead of number
except ValueError:
    print("Error: Please enter valid numbers.")
#user enters 0 for their second number
except ZeroDivisionError:
    print("Error: Cannot divide by zero (0).")
else:
    # if the code works --> show the result
    print(f"The result is: {result}") #move from the try section
finally:
    #indicate that the try-except is complete
    print("Calculation attempt completed.")

# Real World Example - Withdraw money from bank
class InsufficientFundsError(Exception):
    '''
    Exception raised when a withdrawal would result in a negative balance
    '''
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds available")
    return balance - amount

#first one crashes/stops program because it didn't pass the test
#print(withdraw(50, 200)) # I only have 50 so I CAN'T take out 200
print(withdraw(500, 200)) # i have 500 so I can take out 200

#Raise - allows programmer to create their own error messaging
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is unrealistically high!")
    return f"Age set to {age}"

#print(set_age(-4)) #would crash the program -- Age cannot be negative
#print(set_age(121)) #would crash the program -- Age is unrealistically high
print(set_age(50)) #code works


# Real World example: Student Grade Entry
# Try Except in a loop
#function to enter a grade
def get_student_grade():
    #Continue to run this until you have entered a valid grade
    while True: 
        #try-except to catch any errors
        try:
            grade = float(input("Enter student grade (0-100): "))
            #if the grade is between 0 adn 100 --> it is good
            if 0<= grade <= 100:
                return grade
            #otherwise - send message to fix it and run again. 
            else: 
                print("Grade must be between 0 and 100.")
        #User trys to enter a string or non-number value
        except ValueError:
            #explain why their entry was wrong. 
            print("Please enter a numeric value.")

# Requests a student grade and outputs this message
print(f"The student grade is {get_student_grade()}")