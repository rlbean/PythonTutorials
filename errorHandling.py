def get_student_grade():
    while True:
        try:
            grade = float(input("Enter student grade (0-100): "))
            if 0<= grade <= 100:
                return grade
            else: 
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Please enter a numeric value.")

print(f"The student grade is {get_student_grade()}")

"""
class InsufficientFundsError(Exception):
    '''
    Exception raised when a withdrawal would result in a negative balance
    '''
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("Not enough funds available")
    return balance - amount

print(withdraw(500, 200))
"""
'''
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 120:
        raise ValueError("Age is unrealistically high!")
    return f"Age set to {age}"


print(set_age(121))
'''
'''
try:
    #Get user input
    num1 = int(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
except ValueError:
    print("Error: Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero (0).")
else:
    print(f"The result is: {result}") #move from the try section
finally:
    print("Calculation attempt completed.")'
'''