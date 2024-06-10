# import sqlite3

# def create_tables():
#     conn = sqlite3.connect('magazine.db')
#     cursor = conn.cursor()

#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS authors (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL
#     )
#     ''')

   
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS magazines (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT NOT NULL,
#         category TEXT NOT NULL
#     )
#  ''')

   
#     cursor.execute('''
#     CREATE TABLE IF NOT EXISTS articles (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         title TEXT NOT NULL,
#         author_id INTEGER,
#         magazine_id INTEGER,
#         FOREIGN KEY(author_id) REFERENCES authors(id),
#         FOREIGN KEY(magazine_id) REFERENCES magazines(id)
#     )
#     ''')

#     conn.commit()
#     conn.close()

# if _name_ == '_main_':
#     create_tables()