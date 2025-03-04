#Real World Example of Tuple Slicing: Movie Playlist

# Create a tuple of movies
movieList = ("Cinderella", "Alice in Wonderland", "Peter Pan",
             "101 Dalmations", "A Bug's Life", "The Lion King",
             "Hercules", "Atlantis", "Chicken Little")

# Basic slicing examples
print(f"First 3 movies: {movieList[:3]}")
print(f"Last 3 movies: {movieList[-3:]}")
print(f"Movies from index 2 to 5: {movieList[2:6]}")

# Slicing with step 
print(f"Every other movie: {movieList[::2]}")
print(f"Reverse the list: {movieList[::-1]}")

#Practical scenario: List Management
def createWeekendPlaylist(fullList, start, end):
    """ # this is an open multi-line comment
    Create a weekend movie playlist slide
    
    Parameters:
    fullList --> Complete movie list
    start (int) --> starting index of the weekend movies
    end (int) --> ending index of the weekend movies
    """#ends the multi-line comments

    return fullList[start:end]

# Create a weekend playlist
weekendPlaylist = createWeekendPlaylist(movieList, 2, 6)
print("\nWeekend Movie Playlist:")
for i, movie in enumerate(weekendPlaylist, 1):
    print(f"{i}. {movie}") # makes a numbered list

#Advanced slicing --> categorize the movies
classicMovies = movieList[:3] # grabs 0, 1, 2 - first 3
animalMovies = movieList[3:6] # grabs 3, 4, 5 - middle 3
fiaryTaleMovies = movieList[-3:] # grabs 6, 7, 8 - last 3

print(f"Classic Movie Collection: {classicMovies}")
print(f"Movies with Animals: {animalMovies}")
print(f"Fairy Tale Movies: {fiaryTaleMovies}")