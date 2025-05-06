# Class to represent a movie
class Movie:
    def __init__(self, title, director, year, duration):
        # Initialize movie properties
        self.title = title  # Movie title
        self.director = director  # Movie director
        self.year = year  # Release year
        self.duration = duration  # Duration in minutes

    def __repr__(self):
        # Official string representation of the object (for developers)
        return f"Movie(title='{self.title}', director='{self.director}', year={self.year}, duration={self.duration})"

    def __str__(self):
        # User-friendly string representation of the object
        return f"'{self.title}' directed by {self.director} ({self.year}) - {self.duration} min"

    def __len__(self):
        # Return duration of the movie (used by len())
        return self.duration

    def __del__(self):
        # Called when the object is deleted
        print(f"Movie '{self.title}' has been deleted.")

    def __eq__(self, other):
        # Check if two movies are equal (by title and director)
        if not isinstance(other, Movie):
            return NotImplemented
        return self.title == other.title and self.director == other.director

    def __lt__(self, other):
        # Less than comparison based on duration (for sorting)
        if not isinstance(other, Movie):
            return NotImplemented
        return self.duration < other.duration

# Example usage
movie1 = Movie("Inception", "Christopher Nolan", 2010, 148)  # Create movie object
movie2 = Movie("Interstellar", "Christopher Nolan", 2014, 169)
movie3 = Movie("Inception", "Christopher Nolan", 2010, 148)

print(repr(movie1))  # Developer-friendly representation
print(str(movie1))   # User-friendly representation

print(len(movie1))   # Length of the movie (duration)

print(movie1 == movie3)  # True (same title and director)
print(movie1 == movie2)  # False

print(movie1 < movie2)   # True (movie1 duration < movie2 duration)

movies = [movie1, movie2]
movies.sort()  # Sort movies by duration (uses __lt__)
for m in movies:
    print(m)

del movie1  # Delete movie1 object
