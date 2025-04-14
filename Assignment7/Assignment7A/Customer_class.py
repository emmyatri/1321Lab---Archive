#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment7A Customer_class

# customer_class.py

class Customer:
    def __init__(self, name):
        self.name = name
        self.rented_movies = []

    def rent_movie(self, movie):

        if len(self.rented_movies) >= 2:
            return "Rental limit reached"

        if movie in self.rented_movies:
            return "Movie already rented by this customer"

        if movie.is_rented:
            return "Movie already rented by someone else"


        movie.rent()
        self.rented_movies.append(movie)
        return "Movie rented successfully"

    def return_movie(self, movie):

        if movie not in self.rented_movies:
            return "Movie not rented by this customer"

        movie.return_movie()
        self.rented_movies.remove(movie)
        return "Movie returned successfully"