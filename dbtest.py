import sqlite3
import cPickle


con = sqlite3.connect('faces.db')
c= con.cursor()

c.execute("SELECT * FROM faces")
# q=c.fetchall() or
# q=c.fetchone()

print("faces")
for i in c:
    print i

c.execute("SELECT * FROM people")
print("people")
for i in c:
    print i

c.execute("SELECT * FROM svm")
print("svm")
for i in c:
    print i
