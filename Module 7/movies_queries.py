# Justin Marucci
# Assignment 7

import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="movies_user",      
    password="popcorn",  
    database="movies"          
)

# Create a cursor object
cursor = db.cursor()

# 1st Query: Select all fields from the studio table
cursor.execute("SELECT * FROM studio;")
studios = cursor.fetchall()
print("----- Studios Table -----")
for studio in studios:
    print(studio)

print("\n")

# 2nd Query: Select all fields from the genre table
cursor.execute("SELECT * FROM genre;")
genres = cursor.fetchall()
print("----- Genres Table -----")
for genre in genres:
    print(genre)

print("\n")

# 3rd Query: Select film names with a run time of less than two hours
cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120;")
short_movies = cursor.fetchall()
print("----- Movies with runtime less than 2 hours -----")
for movie in short_movies:
    print(movie[0])

print("\n")

# 4th Query: Get a list of film names grouped by director
cursor.execute("SELECT film_director, GROUP_CONCAT(film_name SEPARATOR ', ') FROM film GROUP BY film_director;")
directors_movies = cursor.fetchall()
print("----- Films grouped by Director -----")
for director in directors_movies:
    print(f"Director: {director[0]} | Films: {director[1]}")

# Close the cursor and connection
cursor.close()
db.close()

