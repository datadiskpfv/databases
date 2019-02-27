import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES ('Paul', 123456, 'paul.valle@example.com')")
db.execute("INSERT INTO contacts VALUES ('Lorraine', 987654, 'lorraine.valle@example.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

# print(cursor.fetchall())    # A list containing tuples of each row
# print(cursor.fetchone())    # fetch one row which will be a tuple

for name, phone, email in cursor:
    print("{}, {}, {}".format(name, phone, email))

db.commit()
db.close()
