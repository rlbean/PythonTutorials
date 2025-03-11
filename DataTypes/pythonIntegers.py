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




