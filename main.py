# main.py
from theater import *

movies = get_movies()
tickets = [5, 5, 5, 5, 5]

while any(tickets):
    show_listing(movies, tickets)
    selection = int(input("Which movie do you want to see? > "))
    
    if 1 <= selection <= len(movies):
        buy_ticket(selection, tickets, movies)  # Pass the 'movies' list as the third argument
    else:
        print("Invalid choice. Please choose again.")

print("THE ENTIRE THEATER IS SOLD OUT")


