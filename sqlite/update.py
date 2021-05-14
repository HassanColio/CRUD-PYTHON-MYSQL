import sqlite3
conn = sqlite3.connect('customer.db')
conn.execute("UPDATE customers s WHERE fist_name =jmarry;")
conn.commit()
cursor = conn.execute("SELECT * from customers")
print(cursor.fetchall())
conn.close()