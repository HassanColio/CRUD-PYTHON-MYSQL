import sqlite3

conn = sqlite3.connect('customer.db')
cursor = conn.execute("SELECT * from customers")
print (cursor.fetchall())
conn.close()