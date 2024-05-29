import sqlite3

conn = sqlite3.connect('cars.dp')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS cars(
    id INTEGER PRIMARY KEY, 
    name_cars TEXT NOT NULL,
    model TEXT,
    hp REAL
)
''')

cursor.execute('''
    INSERT INTO cars(name_cars, model, hp)
    VALUES('Tayota', 'supra mk4', 1000 ),
     ('BMW','m5 f90', 790),
      ('Mercedes','AMG 63', 800 )
''')

conn.commit()


cursor.execute('SELECT * from cars')

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()