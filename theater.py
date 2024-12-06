def get_movies():
    return ["Green Book", "Isn't it Romantic", "Arctic", "A Star is Born", "Ralph Breaks the Internet"]

movies = get_movies()
tickets = [5, 5, 5, 5, 5]


def show_listing(showings, tix):
    print("Here are the movies available:")
    for i, movie in enumerate(showings, start=1):
        if tix[i - 1] > 0:  # Adjust the index here
            print(f"{i} - {movie} has {tix[i - 1]} tickets")
        else:
            print(f"{i} - {movie} *SOLD OUT*")

def buy_ticket(movie, tix, movies):
    if 1 <= movie <= len(movies) and tix[movie - 1] > 0:
        print(f"You've purchased a ticket for {movies[movie - 1]}. Enjoy the show!")
        tix[movie - 1] -= 1
    elif 1 <= movie <= len(movies):
        print("ALERT: That movie is sold out. Choose again.")
    else:
        print("Invalid choice. Please choose again.")