import sqlite3
conn = sqlite3.connect('my_app.db')

#if the database doesnt exist when the code is started this creates the database with the needed tables and pieces of data needed for the code to work
def creat_db():
        query = (''' 
                 CREATE TABLE user
                 (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 last_name TEXT NOT NULL,
                 username TEXT NOT NULL, 
                 password TEXT NOT NULL,
                 email TEXT NOT NULL,
                 phone_number INTEGER NOT NULL,
                 kids INTEGER NOT NULL,
                 salary INTEGER NOT NULL,
                 currency TEXT NOT NULL,
                 country_id INTEGER NOT NULL,
                 FOREIGN KEY(country_id) REFERENCES country(id)
                 )
                 '''
                )
        conn.execute(query)

        query = ('''
                 CREATE TABLE country
                 (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 phone_code TEXT NOT NULL,
                 currency TEXT NOT NULL
                 )
                '''
                )
        conn.execute(query)

        query = ('''
                 CREATE TABLE bracket
                 (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 country_id INTEGER NOT NULL,
                 lower_bound INTEGER NOT NULL,
                 upper_bound INTEGER NOT NULL,
                 percentage INTEGER NOT NULL,
                 FOREIGN KEY(country_id) REFERENCES country(id)
                 )
                '''
                )
        conn.execute(query)

        query = ('''
                CREATE TABLE history
                (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 user_id INTEGERN NOT NULL,
                 date INTEGER NOT NULL, 
                 tax_amount REAL NOT NULL, 
                 FOREIGN KEY(user_id) REFERENCES user(id)
                )
                '''
                 )

        conn.execute(query)
        countries = [(1, "Spain", "+34", "EUR"), (2, "United States", "+1", "USD"), (3, "Japan", "+81", "YEN"), (4, "Germany", "+49", "EUR"), (5, "United Kingdom", "+44", "GBP"), (6, "France", "+33", "EUR"), (7, "India", "+91", "INR"), (8, "Brazil", "+55", "BRL"), (9, "South Korea", "+82", "KRW"), (10, "Italy", "+39", "EUR"), (11, "Canada", "+1", "CAD"), (12, "Australia", "+61", "AUD"), (13, "Saudi Arabia", "+966", "SAR"), (14, "Turkey", "+90", "TRY")]
        conn.executemany("INSERT INTO country (id, name, phone_code, currency) \
                         VALUES (?, ?, ?, ?)", countries)

        brackets = [(1, 0, 12450, 19), (1, 12451, 20200, 24), (1, 20201, 35200, 30), (1, 35201, 60000, 37), (1, 60001, 300000, 45), (1, 300001, 1000000000000000, 47),
                    (2, 0, 11000, 10), (2, 11001, 44725, 12), (2, 44726, 95375, 22), (2, 95376, 182100, 24), (2, 182101, 231250, 32), (2, 231251, 578125, 35), (2, 578126, 1000000000000000, 37),
                    (3, 0, 1950000, 5), (3, 1950001, 3300000, 10), (3, 3300001, 6950000, 20), (3, 6950001, 9000000, 23), (3, 9000001, 18000000, 33), (3, 18000001, 40000000, 40), (3, 40000000, 1000000000000000, 45), 
                    (4, 0, 10908, 0), (4, 10909, 25908, 14), (4, 25909, 40908, 23), (4, 40909, 62809, 35), (4, 62810, 277825, 42), (4, 277826, 1000000000000000, 45),
                    (5, 0, 12570, 0), (5, 12571, 50270, 20), (5, 50271, 125140, 40), (5, 125140, 1000000000000000, 45), 
                    (6, 0, 10777, 0), (6, 10778, 27478, 11), (6, 27479, 78570, 30), (6, 78571, 168994, 41), (6, 168995, 1000000000000000, 45),
                    (7, 0, 250000, 0), (7, 250001, 500000, 5), (7, 500001, 750000, 10), (7, 750001, 1000000, 15), (7, 1000001, 1250000, 20), (7, 1250001, 1500000, 25), (7, 1500001, 1000000000000000, 30), 
                    (8, 0, 1904, 0), (8, 1905, 2827, 7.5), (8, 2828, 3751, 15), (8, 3751, 4665, 22.5), (8, 4666, 1000000000000000, 27.5), 
                    (9, 0, 14000, 6), (9, 14001, 50000, 15), (9, 50001, 88000, 24), (9, 88001, 150000, 35), (9, 150001, 300000, 38), (9, 300001, 500000, 40), (9, 500001, 1000000, 42), (9, 1000000, 1000000000000000, 45), 
                    (10, 0, 15000, 23), (10, 15001, 28000, 25), (10, 28001, 50000, 35), (10, 50001, 1000000000000000, 45), 
                    (11, 0, 53359, 15), (11, 53360, 106717, 20.5), (11, 106718, 165430, 26), (11, 165431, 235675, 29), (11, 235676, 1000000000000000, 33), 
                    (12, 0, 18200, 0), (12, 18201, 45000, 19), (12, 45001, 120000, 32.5), (12, 120001, 180000, 37), (12, 180001, 1000000000000000, 45), 
                    (13, 0, 1000000000000000, 20), 
                    (14, 0 , 70000, 15), (14, 70001, 150000, 20), (14, 150001, 370000, 27), (14, 370001, 1900000, 35), (14, 1900000, 1000000000000000, 40)]
        conn.executemany("INSERT INTO bracket (country_id, lower_bound, upper_bound, percentage) \
                     VALUES (?, ?, ?, ?)", brackets)

        conn.commit()
        conn.close()
