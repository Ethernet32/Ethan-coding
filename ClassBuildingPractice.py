class Movie:
    def __init__(self,title, time, director, rating, genre, cast ):
        self.title=title
        self.time=time
        self.director=director
        self.rating=rating
        self.genre=genre
        self.cast=cast
    def __str__(self):
        return f"Name: {self.title}\ntime: {self.time}\nDirector:{self.director}\nRating:{"Rated"+self.rating}\nGenre:{self.genre}\nCast:{self.cast}"
    def sort(self,other):
        n=other.time
        for i in range(n):
            swap=False
            for j in range( 0,n-i-1):
                if other.time >= other.time:
                    other.time, other.time = other.time, other.time
                    swap=True
            if (swap == False):
                break
        return other.time

        

        
mov1=Movie("The Shawshank Redemption", 1994, "Frank Darabont", "R", "Drama", ["Tim Robbins", "Morgan Freeman"])

mov2=Movie("Pulp Fiction", 1994, "Quentin Tarantino", "R", "Crime", ["John Travolta", "Uma Thurman", "Samuel L. Jackson"])

mov3=Movie("The Godfather", 1972, "Francis Ford Coppola", "R", "Crime", ["Marlon Brando", "Al Pacino", "James Caan"])

mov4=Movie("Inception", 2010, 'Christopher Nolan', "PG-13", "Sci-Fi", ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Ellen Page"])

mov5=Movie("The Matrix", 1999, "Lana Wachowski, Lilly Wachowski", "R", "Sci-Fi", ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"])

mov6=Movie("Forrest Gump", 1994, "Robert Zemeckis", "PG-13", "Drama", ["Tom Hanks", "Robin Wright", "Gary Sinise"])

mov7=Movie("The Dark Knight", 2008, "Christopher Nolan", "PG-13", "Action", ["Christian Bale", "Heath Ledger", "Aaron Eckhart"])

mov19=Movie("Schindler's list", 1993, "Steven Spielberg", "R", "Drama", ["Liam Neeson", "Ben Kingsley", "Ralph Fiennes"])

mov8=Movie("Fight Club", 1999, "David Fincher", "R", "Drama", ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"])

mov9=Movie("Goodfellas", 1990, "Martin Scorsese", "R", "Crime", ["Robert De Niro", "Ray Liotta, Joe Pesci"])

mov10=Movie("The Silence of the Lambs", 1991, "Jonathan Demme", "R", "Thriller", ["Jodie Foster", "Anthony Hopkins", "Scott Glenn"])

mov11=Movie("Titanic", 1997, "James Cameron", "PG-13", "Romance", ["Leonardo DiCaprio", "Kate Winslet", "Billy Zane"])

mov12=Movie("Memento", 2000, "Christopher Nolan", "R", "Thriller", ["Guy Pearce", "Carrie-Anne Moss", "Joe Pantoliano"])

mov12=Movie("Gladiator", 2000, "Ridley Scott", "R", "Action", ["Russell Crowe", "Joaquin Phoenix", "Connie Nielsen"])

mov13=Movie("The Green Mile", 1999, "Frank Darabont", "R", "Drama", ["Tom Hanks", "Michael Clarke Duncan", "David Morse"])

mov14=Movie("Alien", 1979, "Ridley Scott", "R", "Horror", ["Sigourney Weaver", "Tom Skerritt", "John Hurt"])

mov15=Movie("Jurassic Park", 1993, "Steven Spielberg", "PG-13", "Adventure", ["Sam Neill", "Laura Dern", "Jeff Goldblum"])

mov16=Movie("The Departed", 2006, "Martin Scorsese", "R", "Crime", ["Leonardo DiCaprio", "Matt Damon", "Jack Nicholson"])

mov17=Movie("The Lion King", 1994, "Roger Allers, Rob Minkoff", "G", "Animation", ["Matthew Broderick", "Jeremy Irons", "James Earl Jones"])

mov18=Movie("The Truman Show", 1998, "Peter Weir", "PG", "Drama", ["Jim Carrey", "Laura Linney", "Noah Emmerich"])

mov20=Movie("The Breakfast Club", 1985, "John Hughes", "R", "Comedy", ["Molly Ringwald", "Emilio Estevez", "Judd Nelson"])

print(mov1.sort(mov3))