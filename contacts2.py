import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = "update2@example.com"
phone = input("Please enter phone number")

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"

# cursors do not commit
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))  # for single value notice comma (<value1>,)
print("{} rows updated".format(update_cursor.rowcount))

# use the below to commit the change
# update_cursor.connection.commit()
update_cursor.close()

# a cursor is actually returned
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print("{}, {}, {}".format(name, phone, email))

db.close()
