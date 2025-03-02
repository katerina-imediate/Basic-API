import sqlite3

## Create a connection to the database
conn = sqlite3.connect('users.db')

## Create a cursor object to execute SQL statements
cursor = conn.cursor()
print('DB Init')

query = 'select sqlite_version();'
cursor.execute(query)

## Fetch and output result
result = cursor.fetchall()
print('SQLite Version is {}'.format(result))

## Create a table called "users"
cursor.execute('''CREATE TABLE users(
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    email TEXT,
                    address TEXT
                )''')
## Insert sample data into the "users" table
cursor.execute('''INSERT INTO users VALUES ('1', 'John Doe', 'johndoe@example.com', 'England'),
('2' ,'Jane Smith', 'janesmith@example.com', 'Germany'),('3', 'Bob Johnson', 'bobjohnson@example.com', 'France')''')

## Display data inserted
print("Data Inserted in the table: ")
data=cursor.execute('''SELECT * FROM users''')
for row in data:
    print(row)

## Commit the changes to the database
conn.commit()

## Close the cursor and the database connection
cursor.close()
conn.close()