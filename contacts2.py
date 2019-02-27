import sqlite3

db = sqlite3.connect("contacts.sqlite")

update_sql = "UPDATE contacts SET email = 'update@example.com' WHERE contacts.phone = 123456"

# cursors do not commit
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

# use the below to commit the change
# update_cursor.connection.commit()
update_cursor.close()

# a cursor is actually returned
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print("{}, {}, {}".format(name, phone, email))

db.close()
