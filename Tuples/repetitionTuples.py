# Real world example of Tuple Repetition: Event Seating and Scheduling

#Tuple of weekdays for a multi-day conference. 
conference_days = ("Monday", "Tuesday", "Wednesday")

#Basic repetition demon
print("Repeating Conference Days:")
print(conference_days * 2) 
# ('Monday', 'Tuesday', 'Wednesday', 'Monday', 'Tuesday', 'Wednesday')

#Practical scenario: Creating a repeated schedule
def generateEventSchedule(event_topics, num_repetitions):
    """
    Generates a repeated event schedule for multiple sessions.

    Args:
    event_topics (tuple): Tuple of even topics
    num_repetitions (int): number of times to repeat the schedule

    """

    # Repeat the event topics
    repeated_schedule = event_topics * num_repetitions
    

    print("\nFull Conference Schedule:")
    #make a list -- loop includes 2 items day and topic
    #enumerate works through whole tuples combo. 
    for day, topic in enumerate(repeated_schedule, 1):
        print(f"Day {day}: {topic}")
        # Day 1: Machine Learning Fundamentals
        # Day 2: Cloud Computing Strategies
        # Day 3: Cybersecurity Innovations
        # Day 4: Machine Learning Fundamentals...

    return repeated_schedule # send this out

# Tuple of event topics
tech_conference_topics = (
    "Machine Learning Fundamentals",
    "Cloud Computing Strategies",
    "Cybersecurity Innovations"
)

#Generate a week-long conference schedule with repeated topics. 
weekly_schedule = generateEventSchedule(tech_conference_topics, 3)

#Additional practical uses: Creating a repeated team assignments
teamMembers = ("Alice","Bob", "Charlie")
teamRotations = teamMembers * 3

print("\nTeam Rotation Schedule:")
for i, member in enumerate(teamRotations, 1):
    print(f"Rotation {i}: {member}")
    # Rotation 1: Alice
    # Rotation 2: Bob
    # Rotation 3: Charlie
    # Rotation 4: Alice...

# Demonstrating different repetition scenarios
print("\n Repetition Examples:")
print(f"Original Tuple: {tech_conference_topics}")
print(f"Repeated Once: {tech_conference_topics * 1}") # listed 1 time only
print(f"Repeated Twice: {tech_conference_topics * 2}") # listed 2 times
print(f"Repeated Zero Times: {tech_conference_topics * 0}") # empty ()