import sqlite3
import text_analyzer

conn = sqlite3.connect('word_db.db')
c = conn.cursor()

'''
c.execute('DROP TABLE Words')
c.execute('DROP TABLE Pos_Types')
c.execute('DROP TABLE Inflections')
'''

c.execute('''CREATE TABLE Words (
                wordID INTEGER PRIMARY KEY,
                word TEXT,
                pos TEXT
            )''')

c.execute('''CREATE TABLE Pos_Types (
                pos TEXT PRIMARY KEY
            )''')

c.execute('''CREATE TABLE Inflections (
                wordID INTEGER,
                inflectedForm TEXT,
                FOREIGN KEY (wordID) REFERENCES Words(wordID)
            )''')

conn.commit()


words = text_analyzer.analyze('text.txt')

'''
for word_inf, details in words.items():
    print(word_inf, '>>>', details)
'''

pos = set([v[0] for v in words.values() if v[0] is not None])
for i in pos:
    c.execute('''INSERT INTO Pos_Types VALUES (?)''', (i, ))
    conn.commit()


id = 1
for word_inf, details in words.items():
    c.execute('''INSERT INTO Words VALUES (?, ?, ?)''',
              (id, word_inf, details[0]))
    for inf in details[1]:
        c.execute('''INSERT INTO Inflections VALUES (?, ?)''', (id, inf))
    id += 1
    conn.commit()


'''
Виводимо всі дані таблиці слів:
c.execute("SELECT * FROM Words")
result = c.fetchall()

for row in result:
    print(row)


#Виводимо всі прикметники:
c.execute("SELECT * FROM Words WHERE pos='ADJF'")
result = c.fetchall()

for row in result:
    print(row)
'''

conn.close()
