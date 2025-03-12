# Real World Examples of Floating Point numbers in Python Programming

# 1 - Price and Currency  Calculations
def calculate_total_price(item_price, quantity, tax_rate=0.12):
    """
    Calculate total price including 12% taxes
    7% PST & 5% GST
    """
    subtotal = item_price * quantity
    tax_amount = subtotal * tax_rate
    total = subtotal + tax_amount

    return subtotal, tax_amount, total

# Example 
shirt_price = 24.99
quantity = 3
subtotal, tax, total = calculate_total_price(shirt_price, quantity)

print("Shopping Cart:")
print(f"Item price: ${shirt_price:.2f}") #$24.99
print(f"Quantity: {quantity}") # 3
print(f"Subtotal: ${subtotal:.2f}") #$74.97
print(f"Tax (12%): ${tax:.2f}") # $9.00
print(f"Total: ${total:.2f}\n") # $83.97

# 2 - Scientific Measurements and Conversions
def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Calsius to Fahrenheit
    """
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius
    """
    return (fahrenheit - 32) * 5/9


# Example temperature conversions
body_temp_c = 37.0
room_temp_c = 22.5
freezing_f = 32.0

print("Temperature Conversions:")
print(f"Body Temperature: {body_temp_c}°C = {celsius_to_fahrenheit(body_temp_c):.1f}°F")
print(f"Room Temperature: {room_temp_c}°C = {celsius_to_fahrenheit(room_temp_c):.1f}°F")
print(f"Freezing point: {freezing_f}°F = {fahrenheit_to_celsius(freezing_f):.1f}°C")

# 3 - Financial Calculations: Compound Interest
def calculate_compound_interest(principal, rate, years, compounds_per_year=1):
    """
    Calculate the final amount with compound interest
    """
    rate_decimal = rate / 100 # Covert percentage to decimal
    n = compounds_per_year
    t = years

    # Compound interest formula: A = P(1 + r/n) ^ (nt)
    amount =principal * (1 + (rate_decimal / n)) ** (n * t)
    interest_earned = amount - principal
    return amount, interest_earned

# Example investment calculations
investment = 1000.00
interest_rate = 5.25
time_period = 10

print("Investment Growth:")
print(f"Initial investment: {investment:.2f}")
print(f"Interest rate: {interest_rate}%")
print(f"Time period: {time_period} years")
print(f"Final amount: ")