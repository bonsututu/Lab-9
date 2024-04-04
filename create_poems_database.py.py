import sqlite3

# Connect to the database (this will create the database file if it doesn't exist)
conn = sqlite3.connect('poems.db')

# Create a cursor object to execute SQL commands
c = conn.cursor()

# SQL command to create the 'poems' table
create_table_sql = """
CREATE TABLE IF NOT EXISTS poems (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    text TEXT
)
"""

# Execute the SQL command to create the table
c.execute(create_table_sql)

# List of poems to insert into the database
poems = [
    ('The Road Not Taken', 'Robert Frost', 'Two roads diverged in a yellow wood, And sorry I could not travel both...'),
    ('Ozymandias', 'Percy Bysshe Shelley', 'I met a traveller from an antique land Who said: Two vast and trunkless legs of stone...'),
    ('Daffodils', 'William Wordsworth', 'I wandered lonely as a cloud That floats on high o''er vales and hills...'),
    ('Sonnet 18', 'William Shakespeare', 'Shall I compare thee to a summer''s day? Thou art more lovely and more temperate...'),
    ('The Raven', 'Edgar Allan Poe', 'Once upon a midnight dreary, while I pondered, weak and weary...')
]

# SQL command to insert poems into the 'poems' table
insert_poems_sql = "INSERT INTO poems (title, author, text) VALUES (?, ?, ?)"

# Execute the SQL command to insert poems into the table
c.executemany(insert_poems_sql, poems)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database created and populated successfully.")
