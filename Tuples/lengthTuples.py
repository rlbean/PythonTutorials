# Real World example of Tuple Length: Product Inventory

# Tuple of product inventory
# Each product contains a tuple --> 
# (productID, productName, quantity, price)

#fill inventory Tuple
inventory = (
    # ID      Product Name          #  Price
    ("A001", "Wireless Headphones", 50,129.99),
    ("B002", "Smart Watch", 30, 199.50),
    ("C003", "Bluetooth Speakers", 75, 79.99),
    ("D004", "Portable Charger", 100, 49.99),
    ("E005", "Noise-Canceling Earbuds", 25, 249.99)
)

# Basic length demonstration
print(f"Total number of products in inventory: {len(inventory)}")
# counts the items in the inventory -- item types not individual items

# Practical inventory management function
def checkInventoryStatus(inventory):
    """multi-line comment

    Analyzes the inventory to determine its status and potential revenue

    Categorizes the inventory based on the number of products
    and calculates the total potential revenue

    Args: 
    inventory (tuple): Tuple of tuple products
    """

    totalProducts = len(inventory)

    #Categorize inventory size
    # product item listing -- headphones, smart watch, speaker, charger, earbuds
    if totalProducts < 3:
        status = "Low stock"
    elif 3 <= totalProducts < 6:
        status = "Moderate Stock"
    else:
        status = "Well Stocked"

    # Calculate total potential revenue
    total_potential_revenue = sum(product[2] * product[3] for product in inventory)
    # sum() -- adds all of the elements you have inside. 
    # product[2] * product[3] for product in inventory
    # a loop that runs through each item in the inventory
    # takes the total number of that item
    # multiplies it by the price per item
    # ie. Headphones - 50 items * 129.99 each = $6,499.50
    # then Watch - 30 * 199.50 = $5,985.00

    return { # it returns out the inner tuple of information for each
        "total_products": totalProducts,
        "inventory_status": status,
        "total_potential_revenue": round(total_potential_revenue, 2)
    }

# Get inventory analysis
inventory_analysis = checkInventoryStatus(inventory)

# Display inventory information
print("\nInventory Analysis:")
#grabs the total items in our overall list -- 5
print(f"Total Number of Products: {inventory_analysis['total_products']}")
# checks the status -- do we have enough variety of items
print(f"Inventory Status: {inventory_analysis['inventory_status']}")
# calculates the potential earnings of our objects
print(f"Total Potential Revenue: ${inventory_analysis['total_potential_revenue']:,.2f}")

# Demonstrating length in conditional logic

# Demo length in conditional logic
if len(inventory) > 4:
    print("\nGreat! We have a diverse product range.")
else:
    print("\nConsider expanding our product lineup.")