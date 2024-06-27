import sqlite3

def netflix():
    con = sqlite3.connect('netflix_columns.db')
    cursor = con.cursor()
    
    cursor.execute(
        '''
        CREATE TABLE netflix_titles(
            show_id NUMBER(10),
            type VARCHAR(10),
            tittle VARCHAR(90),
            cast VARCHAR2(90),
            country VARCHAR2(20),
            date_added DATE,
            release_year DATE,
            rating VARCHAR2(10),
            duration NUMBER(90),
            listed_id VARCHAR2(90),
            description VARCHAR2(90)
        )
        ''')
    cursor.execute("""INSERT INTO netflix_titles VALUES('s1', 'TV SHOW', '', 
        'Jo√£o Miguel, Bianca Comparato, Michel Gomes, Rodolfo Valente, Vaneza Oliveira, Rafael Lozano, Viviane Porto, Mel Fronckowiak, Sergio Mamberti, Zez√© Motta, Celso Frateschi',
        'Brazil',
        'August 14, 2020',
        '2020',
        'TV-MA',
        4,
        'International TV Shows, TV Dramas, TV Sci-Fi & Fantasy',
        'In a future where the elite inhabit an island paradise far from the crowded slums, you get one chance to join the 3%, saved from squalor.'
        )""")
    
    con.commit()
    for row in cursor.execute('SELECT * FROM netflix_titles'):
        print(row)
    con.close()
netflix()