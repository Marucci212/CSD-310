#Justin Marucci
# Assignment 8

import mysql.connector

# Connect to MySQL database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="movies_user",
    password="popcorn",
    database="movies"
)

# Create cursor
cursor = db.cursor()

# Function to display films
def show_films(cursor, title):
    # Select statement with INNER JOINs to get genre and studio names
    query = (
        "SELECT film_name AS 'Name', film_director AS 'Director', "
        "genre_name AS 'Genre', studio_name AS 'Studio' "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
    )
    cursor.execute(query)
    films = cursor.fetchall()

    print("\n-- {} --".format(title))
    for film in films:
        print("Name: {}\nDirector: {}\nGenre: {}\nStudio: {}\n".format(film[0], film[1], film[2], film[3]))

# 1. Initial display of films
show_films(cursor, "DISPLAYING FILMS")

# 2. Insert a new movie (pick anything you like, using existing studio_id and genre_id)
# Let's insert "Interstellar" directed by "Christopher Nolan", Sci-Fi (genre_id=2), Studio (studio_id=1 for example)
insert_film = (
    "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) "
    "VALUES ('Interstellar', '2014', 169, 'Christopher Nolan', 1, 2)"
)
cursor.execute(insert_film)
db.commit()

# Display after insert
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# 3. Update Alien to be a Horror film (genre_id=1)
update_film = (
    "UPDATE film "
    "SET genre_id = 1 "
    "WHERE film_name = 'Alien'"
)
cursor.execute(update_film)
db.commit()

# Display after update
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Alien to Horror")

# 4. Delete the movie Gladiator
delete_film = (
    "DELETE FROM film "
    "WHERE film_name = 'Gladiator'"
)
cursor.execute(delete_film)
db.commit()

# Display after delete
show_films(cursor, "DISPLAYING FILMS AFTER DELETE - Gladiator")

# Close cursor and connection
cursor.close()
db.close()
