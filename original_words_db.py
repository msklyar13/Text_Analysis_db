import sqlite3

conn = sqlite3.connect('wor_db.db')
c = conn.cursor()

c.execute('''CREATE TABLE Words (
                wordID INTEGER PRIMARY KEY,
                spelling TEXT,
                meaning TEXT,
                posType TEXT,
                examples TEXT
            )''')

c.execute('''CREATE TABLE Pos (
                posType TEXT PRIMARY KEY
            )''')

c.execute('''CREATE TABLE Inflections (
                wordID INTEGER,
                inflectedForms TEXT,
                inflectionType TEXT
            )''')

c.execute('''CREATE TABLE Inflection_Types (
                inflectionType TEXT PRIMARY KEY
            )''')

c.execute('''SELECT Words.spelling AS word,
                    Inflections.inflectedForms AS inflection
                    FROM Words
                    INNER JOIN Inflections ON Inflections.wordID = Words.wordID
            ''')

c.execute('''SELECT Inflection_Types.inflectionType AS infType,
                    Inflections.inflectedForms AS inflection
                    FROM Inflection_Types
                    INNER JOIN Inflections ON Inflections.inflectionType = Inflection_Types.inflectionType
            ''')

c.execute('''SELECT Words.spelling AS word,
                    Pos.posType AS posType
                    FROM Words
                    INNER JOIN Pos ON Pos.posType = Words.posType
            ''')

conn.commit()

conn.close()
