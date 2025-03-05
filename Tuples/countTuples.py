# Real World Example of tuple counting: Election and Survey Analysis

# 1 - Basic Voting Scenario
votes = ("Yes", "No", "No", "No", "Yes", "Yes", "Abstain", "Yes")
print("Voting Results Analysis:")
print(f"Total 'Yes' Votes: {votes.count("Yes")}")
print(f"Total 'No' Votes: {votes.count("No")}")
print(f"Total 'Abstain' Votes: {votes.count("Abstain")}")

# Function to analyse voting results
def analyzeElectionResults(votes_tuple):
    """
    Analyze election results and provide detailed stats

    Args.
    votes_tuple (Tuple): Tuple of vote choices

    """

    #count different vote types
    total_votes = len(votes_tuple)
    yes_votes = votes_tuple.count("Yes")
    no_votes = votes_tuple.count("No")
    abstain_votes = votes_tuple.count("Abstain")

    #Calculate percentages
    yes_percentage = (yes_votes / total_votes) * 100
    no_percentage = (no_votes / total_votes) * 100
    abstain_percentage = (abstain_votes / total_votes) * 100
    print(yes_percentage)

    #Print detailed results
    print("\nElection Result Breakdown:")
    print(f"Total Votes: {total_votes}") # 4 
    print(f"Yes Votes: {yes_votes} ({yes_percentage:.2f}%)") # 4 # 4 (50.00%)
    print(f"No Votes: {no_votes} ({no_percentage:.2f}%)") # 3 (37.50%)
    print(f"Abstain Votes: {abstain_votes} ({abstain_percentage:.2f}%)") # 1 (12.50%)

    #Determine Election Results
    if yes_votes > no_votes:
        print("\nElection Results: Proposal PASSED") ###This one is run
    elif no_votes > yes_votes:
        print("Election Results: Proposal REJECTED")
    else: 
        print("\nElection Results: TIED")

# Run election analysis
analyzeElectionResults(votes)

#Product Inventory Counting
inventory = ("Apple", "Banana", "Apple", "Orange", "Apple", "Banana", "Apple", "Grape", "Orange")
print("\nInventory Count:")
print(f"Number of Apples: {inventory.count("Apple")}") # 4
print(f"Number of Bananas: {inventory.count("Banana")}") # 2
print(f"Number of Oranges: {inventory.count("Orange")}") # 2
print(f"Number of Grapes: {inventory.count("Grape")}") # 1

#Function to analyze inventory
def inventory_analysis(inventory_tuple):
    """
    Provide a detailed inventory analysis
    
    Args:
    inventory_tuple (tuple): Tuple of product items
    """

    #Get unique products
    unique_products = set(inventory_tuple)

    print("\nInventory Detailed Analysis:")
    for product in unique_products:
        product_count = inventory_tuple.count(product)
        product_percentage = (product_count / (len(inventory_tuple))) * 100
        print(f"{product}: {product_count} items ({product_percentage:.2f}%)")
        # {product_percentage:.2f}% -- outputs percentage to 2 decimal places

#Run inventory analysis
inventory_analysis(inventory)

# 3 - Survey Response Analysis
survey_responses = (
    "Satisfied", "Neutral", "Satisfied", "Dissatisfied",
    "Satisfied", "Neutral", "Satisfied", "Dissatisfied"
)

def survey_results_analysis(responses):
    """
    Analyze survey responses and provide insights

    Args:
    responses (tuple): Tuple of syrvey response choices
    """

    total_reponses = len(responses) # 8

    #Count different response types
    satisfied_count = responses.count("Satisfied")
    neutral_count = responses.count("Neutral")
    dissatisfied_count = responses.count("Dissatisfied")

    #Calculate percentages
    satisfied_percentage = (satisfied_count / total_reponses) * 100
    neutral_percenteage = (neutral_count / total_reponses) * 100
    dissatisfied_percentage = (dissatisfied_count / total_reponses) * 100

    print("\nSurvey Response Analysis:")
    print(f"Total Responses: {total_reponses}")
    print(f"Satisfied: {satisfied_count} ({satisfied_percentage:.2f}%)")
    print(f"Neutral: {neutral_count} ({neutral_percenteage:.2f}%)")
    print(f"Dissatisfied: {dissatisfied_count} ({dissatisfied_percentage:.2f}%)")

    #Determine overall satisfaction
    #if the satisfied count is larger than the neutral and dissatified counts. 
    if satisfied_count > neutral_count and satisfied_count > dissatisfied_count:
        print("\nOverall Result: Positive Satisfaction")
    elif dissatisfied_count > satisfied_count: # if dissatisfied count is higher
        print("\nOverall Result: Needs Improvement")
    else:
        print("\nOverall Result: Mixed Feeback")

#Run survey analysis
survey_results_analysis(survey_responses)

# Survey outputs the results based on the responses
# change up the responses to see different results