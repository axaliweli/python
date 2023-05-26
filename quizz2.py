import sqlite3
conn = sqlite3.connect("movies_ranking.sqlite")
cursor = conn.cursor()

#gamogvaqs bazidan yvela filmis informacia romelic gamovida 2009 wels
cursor.execute("SELECT * FROM movies WHERE Year = 2009")
result = cursor.fetchall()
for row in result:
    print(row)


# #inputit sheyvanili filmis monacemebi emateba bazashi execute funqciis daxmarebit. commit funqciis vinaxavt cvlilebas bazashi
# movie = input("pilmis saxeli: ")
# genre = str(input("janri: "))
# lead_studio = str(input("mwarmoebeli studia: "))
# wwg = float(input("shemosavali: "))
# year = int(input("weli: "))
# input = (movie, genre, lead_studio, wwg, year,)
# cursor.execute("INSERT INTO movies (film, genre, leadstudio, worldwidegross, year) VALUES (?, ?, ?, ?, ?)", (input))
# conn.commit()
# print ("filmi damatebulia")

# # inputit sheyvanili filmistvis vcvlit janrs da execute funqciit vaxorcielebt cvlilebas, xolo commit funqcia ninaxavs cvlilebebs bazashi
# movie = input("pilmi romlis janris shecvlac gindat: ")
# new_genre = str(input("axali jnari: "))
# input = (new_genre, movie)
# cursor.execute("UPDATE movies SET genre=? WHERE film=?", (input))
# conn.commit()
# print ("janri ganaxlebulia")


# # inputit archeul pilms vshlit bazidan execute metodis daxmarebit. commit funqcia inaxavs cvlilebas bazashi.
# movie = input("pilmis saxeli romelsac shlit: ")
# cursor.execute("DELETE FROM movies WHERE film=?", (movie,))
# conn.commit()
# print ("pilmi waishala")


conn.close