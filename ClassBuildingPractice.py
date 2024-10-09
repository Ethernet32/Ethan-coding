import time
class Movie:
    def __init__(self,title, time, director, rating, genre, cast ):
        self.title=title
        self.time=time
        self.director=director
        self.rating=rating
        self.genre=genre
        self.cast=cast
    def __str__(self):
        return f"Name: {self.title}\ntime: {self.time}\nDirector:{self.director}\nRating:{self.rating}\nGenre:{self.genre}\nCast:{self.cast}"
    def __lt__(self, other):
        if sortingpick == "a":
            return self.title < other.title
        elif sortingpick == "b":
            return self.time < other.time
        else:
            return "Invalid Input"
    def getgenre(self):
        for j in movies:
            if j.genre == genrePick:
                print(f"Name: {j.title}\ntime: {j.time}\nDirector:{j.director}\nRating:{j.rating}\nGenre:{j.genre}\nCast:{j.cast}")
                print("")
    def getdirector(self):
        for j in movies:
            if j.director == directorPick:
                print(f"Name: {j.title}\ntime: {j.time}\nDirector:{j.director}\nRating:{j.rating}\nGenre:{j.genre}\nCast:{j.cast}")
                print("")
    def getcast(self):
        for j in movies:
            if j.cast == castPick:
                print(f"Name: {j.title}\ntime: {j.time}\nDirector:{j.director}\nRating:{j.rating}\nGenre:{j.genre}\nCast:{j.cast}")
                print("")
movies = [
    Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"]),
    Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"]),
    Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"]),
    Movie("Inception", 2010, 'Christopher Nolan', "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"]),
    Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"]),
    Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"]),
    Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"]),
    Movie("Schindler's list", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"]),
    Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"]),
    Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta, Joe Pesci"]),
    Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"]),
    Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"]),
    Movie("Memento", 2000, "Christopher Nolan", "R", "Thriller", ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"]),
    Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"]),
    Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"]),
    Movie("Alien", 1979, "Ridley Scott", "R", "Horror", ["Sigourney Weaver", "Tom Skerritt", "John Hurt"]),
    Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"]),
    Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"]),
    Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"]),
    Movie("The Truman Show", 1998, "Peter Weir", "PG", "Drama", ["Jim Carrey", "Laura Linney", "Noah Emmerich"]),
    Movie("The Breakfast Club", 1985, "John Hughes", "R", "Comedy", ["Molly Ringwald", "Emilio Estevez", "Judd Nelson"]),
]
while True:
    
    print("\033c")
    sortingpick=input("a. sort movies in alphabetical order\nb. sort movies in chronological order\nc. Search genre \nd.Search director\ne. Search cast\nf. EXIT\n")
    print("\033c")
    if sortingpick == "a":
        print("\033c")
        sortedmovies=sorted(movies)
        for i in sortedmovies:
            print(f"Name: {i.title}\ntime: {i.time}\nDirector:{i.director}\nRating:{i.rating}\nGenre:{i.genre}\nCast:{i.cast}")
            print("")
    elif sortingpick == "b":
        print("\033c")
        sortedmovies=sorted(movies)
        for i in sortedmovies:
            print(f"Name: {i.title}\ntime: {i.time}\nDirector:{i.director}\nRating:{i.rating}\nGenre:{i.genre}\nCast:{i.cast}")
            print("")
    elif sortingpick == "c":
        print("\033c")
        genrePick=input("Pick what genre do you want to Search\nDrama\nCrime\nSci-Fi\nAction\nThrille\nRomance\nFantasy\nComedy\nAnimation\n")
        print("\033c")
        Movie.getgenre(movies)
    elif sortingpick == "d":
        print("\033c")
        print("What director do you want to search for")
        directorPick=input("")
        print("\033c")
        Movie.getdirector(movies)
    elif sortingpick == "e":
        print("\033c")
        print("What cast member do you want to search for")
        castPick=input("")
        Movie.getcast(movies)
    elif sortingpick == "f":
        print("Thank you. Goodbye")
        break
