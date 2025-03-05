# Real World example of Tuple Concatenation (Join): 
# Project Team and Skill Management

# Initial project teams
frontendTeam = ("Alice", "Bob", "Charlie")
backendTeam = ("David", "Eve", "Frank")
designTeam = ("Grace", "Helen", "Ivan")

# Basic concatenate demo (join)
full_dev_team = frontendTeam + backendTeam
print(f"Full Development Team: {full_dev_team}")
#("Alice", "Bob", "Charlie", "David", "Eve", "Frank")

#Practical scenario: Project team formation and skill tracking
def combineProjectTeams(*team_tuples):
    """
    Combines multiple team tuples and provides team insights
    
    Args:
    *team_tuples: Variable number of team tuples to combine

    Returns:
    tuple: Combined team with additional team stats
    """

    #Concatenate all input team tuples
    combinedTeam = ()
    for team in team_tuples:
        combinedTeam += team

    #Team Statistics
    team_stats = (
        f"Total Team Members: {len(combinedTeam)}",
        f"Unique Team Members: {len(set(combinedTeam))}",
        f"First Team Member: {combinedTeam[0]}",
        f"Last Team Member: {combinedTeam[-1]}"
    )

    #Combine team members with team stats
    full_project_info = combinedTeam + team_stats

    return full_project_info

#Combine teams for a new project
projectTeam = combineProjectTeams(frontendTeam, backendTeam, designTeam)

#Display project team details
print("\nProject Team Details:")
for info in projectTeam:
    print(info)
# All names (Alice, Bob, Charlie, David, Eve, Frank, Grace, Helen, Ivan)
# Total Team Members: 9
# Unique Team Members: 9
# First Team Member: Alice
# Last Team Member: Ivan

#Additional concatenation
#Skill Sets for different team members
frontendSkills = ("React", "CSS", "JavaScript")
backendSkills = ("Python", "Django", "SQL")
cloudSkills = ("AWS", "Docker", "Kubernetes")

#Concatenating skill sets
combinedSkills = frontendSkills + backendSkills + cloudSkills
print(f"\nCombined Team Skills: {combinedSkills}")
# lists them all ('React', 'CSS', 'JavaScript', 'Python', 'Django', 'SQL', 'AWS', 'Docker', 'Kubernetes')

#Demo concatentation with repeated tuples
certificationTracks = ("Beginner",) * 3 + ("Intermediate",) * 2 + ("Advanced",)* 1
print(f"\nTraining Certification Tracks: {certificationTracks}")
# ('Beginner', 'Beginner', 'Beginner', 'Intermediate', 'Intermediate', 'Advanced')