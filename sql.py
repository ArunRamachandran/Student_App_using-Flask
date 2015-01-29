import sqlite3

con = sqlite3.connect('student.db')
con.execute("DROP TABLE IF EXISTS student") 
con.execute("CREATE TABLE student(sname TEXT NOT NULL, mark TEXT NOT NULL)")
