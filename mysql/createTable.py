import pymysql

conn = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    password = "",
    charset = 'utf8mb4',
)
try:
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS movies_db")
        cursor.execute("USE movies_db")
        cursor.execute("""CREATE TABLE IF NOT EXISTS movies(
            imdb_id VARCHAR(20) PRIMARY KEY,
            title VARCHAR(500),
            director VARCHAR(200),
            year INT,
            rating FLOAT,
            actors VARCHAR(500),
            description TEXT,
            poster_url VARCHAR(500),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )""")
        print("Table created successfully")

        cursor.execute("""
            INSERT INTO movies (imdb_id, title, director, year, rating, actors, description, poster_url) VALUES
            ('tt0111161', 'The Shawshank Redemption', 'Frank Darabont', 1994, 9.3, 'Tim Robbins, Morgan Freeman, Bob Gunton', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 'https://www.imdb.com/title/tt0111161/mediaviewer/rm1690056449/?ref_=tt_ov_i'),
            ('tt0068646', 'The Godfather', 'Francis Ford Coppola', 1972, 9.2, 'Marlon Brando, Al Pacino, James Caan', 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.', 'https://www.imdb.com/title/tt0068646/mediaviewer/rm746868224/?ref_=tt_ov_i'),
            ('tt0050083', '12 Angry Men', 'Sidney Lumet', 1957, 9.0, 'Henry Fonda, Lee J. Cobb, Martin Balsam', 'The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.', 'https://www.imdb.com/title/tt0050083/mediaviewer/rm2927108352/?ref_=tt_ov_i'),
            ('tt0110912', 'Pulp Fiction', 'Quentin Tarantino', 1994, 8.9, 'John Travolta, Uma Thurman, Samuel L. Jackson', 'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.', 'https://www.imdb.com/title/tt0110912/mediaviewer/rm2927108352/?ref_=tt_ov_i'),
            ('tt0133093', 'The Matrix', 'Lana WachowskiLilly Wachowski, Lilly Wachowski', 1999, 8.7, 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss', 'When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.', 'https://www.imdb.com/title/tt0133093/mediaviewer/rm2927108352/?ref_=tt_ov_i')
        """)
        conn.commit()
        print("Data inserted successfully")
        
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()