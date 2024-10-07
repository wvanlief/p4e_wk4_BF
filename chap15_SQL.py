import sqlite3
import re

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fh = open(r'mbox.txt')

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    orgs = re.findall('@(.+)', pieces[1])[0]
    #email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (orgs,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (orgs,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (orgs,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()