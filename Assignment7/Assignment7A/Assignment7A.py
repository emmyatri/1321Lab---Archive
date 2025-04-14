#Class: CSE 1321L
#Section: P52
#Term: Spring 2025
#Instructor: Roshni Satish
#Name: Amelia Ellingson
#Lab#: Assignment7A

# main.py
from Movie_class import Movie
from Customer_class import Customer

def main():
    # Define a Movie and Customer for testing
    movie1 = Movie("Inception", "Christopher Nolan")
    customer1 = Customer("Ethan")
    # Scenario 1: Ethan rents the movie "Inception"
    print(customer1.rent_movie(movie1))
    # Output: "Movie rented successfully"
    # Scenario 2: Ethan tries to rent "Inception" again
    print(customer1.rent_movie(movie1))
    # Output: "Movie already rented by this customer"
    # Scenario 3: Ethan returns "Inception"
    print(customer1.return_movie(movie1))
    # Output: "Movie returned successfully"
    # Scenario 4: Ethan tries to return "Inception" again
    print(customer1.return_movie(movie1))
    # Output: "Movie not rented by this customer"
    # Scenario 5: Another customer, Olivia, tries to rent "Inception"
    customer2 = Customer("Olivia")
    print(customer2.rent_movie(movie1))
    # Output: "Movie rented successfully"
    # Scenario 6: Ethan tries to rent more than the limit of 2 movies
    # Define more movies
    movie2 = Movie("The Matrix", "Wachowskis")
    movie3 = Movie("Interstellar", "Christopher Nolan")
    # Ethan rents 2 movies
    print(customer1.rent_movie(movie2))
    # Output: "Movie rented successfully"
    print(customer1.rent_movie(movie3))
    # Output: "Movie rented successfully"
    # Ethan tries to rent a third movie
    movie4 = Movie("Avatar", "James Cameron")
    print(customer1.rent_movie(movie4))
    # Output: "Rental limit reached"

if __name__ == "__main__":
    main()