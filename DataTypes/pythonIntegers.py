# Real World Examples of Integers in Python programming

# 1 - Age Calculation and Demographics
def calculate_age_group(birth_year, current_year=2025):
    """
    Calculate age and determine age group category

    Args:
    birthYear (int): birth year of user
    currentYear (int): set in the arguements section as 2025
    """

    # Calculate age (integer math)
    age = current_year - birth_year

    # Determine age group using integer ranges
    if age < 13:
        age_group = "Child"
    elif age < 20:
        age_group = "Teenager"
    elif age < 65:
        age_group = "Adult"
    else:
        age_group = "Senior"
    
    return age, age_group # send out the entered age and the string ageGroup

# Example usage
birthYear = 1995
age, category = calculate_age_group(birthYear)
print(f"A person born in {birthYear} is {age} years old and falls in the '{category}' category. \n")

# 2 - Inventory and Stock Management
current_stock = 157
minimum_stock = 20
reorder_amount = 50

# Check stock levels and determine actions
if current_stock <= minimum_stock:
    print(f"ALERT: Current stock ({current_stock}) below minimum level ({minimum_stock})")
    print(f"Action: Place order for {reorder_amount} more units.")
else:
    remaining_units = current_stock - minimum_stock
    days_supply = remaining_units // 5 # Integer division - assumes 5 units sold per day
    print(f"Stock Status: {current_stock} units in inventory.")
    print(f"Approximately {days_supply} days of supply remaining before reorder needed. \n")

# 3 - Score Calculation and Grading
quiz_scores = [85, 91, 78, 90, 88]
total_score = 0

# Sum calculation with integers
for score in quiz_scores:
    total_score += score # Addition with integers

# Integer division with remainder
num_quizzes = len(quiz_scores)
average_score = total_score // num_quizzes # Integer division
remainder = total_score % num_quizzes #Remainder (modulus operator)

print(f"Quiz Scores: {quiz_scores}")
print(f"Total score: {total_score}")
print(f"Average Score: (integer division): {average_score}")
print(f"Remainder after division: {remainder}")

# More accurate average with floating point 
# --> set number of decimal points
accurate_average = total_score / num_quizzes
print(f"Accurate Averages: {accurate_average:.2f}\n")

# 4 - Currency and Financial Calculations
item_price_cents = 2995 # Stored as interger to avoid floating point errors
quantity = 3

# Money calculations usign integers
total_cents = item_price_cents * quantity
dollars = total_cents // 100 # Integer division to get dollar amount
cents = total_cents % 100 # Modulous (remainder) caclculation to get cents amount

print(f"Item price: {item_price_cents/100:.2f}") # 2 decimal places -- money
print(f"Quantity: {quantity}")
print(f"Total cost: ${dollars}.{cents:02d}") #string formatting to display properly - $89.85
print(f"Alternative format: ${total_cents/100:.2f}\n")

# 5 - Integer in Binary, Octal, and Hexadecimal forms
num = 42
print(f"Decimal: {num}")
print(f"Binary: {bin(num)}") #0b101010
print(f"Octal: {oct(num)}") # 0o52
print(f"Hexadecimal: {hex(num)}\n") # 0x2a

# 6 - Bitwise Operations (used in permissions, flags, etc.)
read_permission = 4 # 100 in binary
write_permission = 2 # 010 in binary
execute_permission = 1 # 001 in binary

#Combining permissions using bitwise OR ( | = OR)
user_permission = read_permission | write_permission # 110 in binary (6)
admin_permission = read_permission | write_permission | execute_permission # 111 in binary (7)

print(f"Read permission: {read_permission} ({bin(read_permission)})")
print(f"Write permission: {write_permission} ({bin(write_permission)})")
print(f"Execute permission: {execute_permission} ({bin(execute_permission)})")
print(f"User permission: ({bin(user_permission)})")
print(f"Admin permission: ({bin(admin_permission)})\n")

# 7 - Time Calcualations (with Integer division)
def convert_seconds(total_seconds):
    """
    Convert seconds to hours, minutes, seconds
    """
    hours = total_cents // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    return hours, minutes, seconds

# Example: Video Length
video_length = 7825 # seconds
hours, minutes, seconds = convert_seconds(video_length) 
print(f"Video Length: {video_length} seconds") # 7825 seconds
print(f"Formatted time: {hours}:{minutes:02d}:{seconds:02d}") # 2:10:25