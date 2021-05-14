import sqlite3
con = sqlite3.connect('task.db')

c = con.cursor()

c.execute("CREATE TABLE task")
