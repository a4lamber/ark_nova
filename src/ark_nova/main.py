import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("./data/ark_nova.db")

# Create a cursor object
cursor = conn.cursor()

# Write a SQL query to create a table without autoincrement
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
);
"""

# Execute the SQL query
cursor.execute(create_table_query)

# Commit the changes
conn.commit()

# Close the connection
conn.close()
