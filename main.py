import sqlite3

conn = sqlite3.connect("movies.db")
conn.execute("DROP TABLE IF EXISTS movies")
conn.execute('CREATE TABLE movies(movie_name STRING, actor_name STRING, actress_name STRING, release_year STRING, '
             'director STRING)')
entries = int(input("enter number of entries: "))

while entries > 0:
    m_name = input("\nenter the Movie's name: ")
    m_actor = input("Enter the Actor's name: ")
    m_actress = input("Enter the Actress's name: ")
    m_director = input("Enter the Director's name: ")
    m_year = input("Enter the year of release: ")
    param = (m_name, m_actor, m_actress, m_year, m_director)
    conn.execute('INSERT INTO movies(movie_name, actor_name, actress_name, release_year, director) VALUES(?,?,?,?,?)',param)

    entries -= 1

cur = conn.cursor()
cur.execute("SELECT * FROM movies")
rows = cur.fetchall()
for row in rows:
    print('\nName of the movie: '+ row[0])
    print('Name of the Actor: '+ row[1])
    print('Name of the Actress: '+ row[2])
    print('Year of Release: '+ str(row[3]))
    print('Name of the Director: '+ row[4])

cur.execute("SELECT movie_name FROM movies WHERE actor_name = 'Robert Downey Junior'")
rows = cur.fetchall()
for row in rows:
    if len(row) is 0:
        print("\nmovie not found")
    else:
        print("\nName of the movie is: "+row[0])
conn.close()