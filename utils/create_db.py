import sqlite3
import os


def create_db(database_filename):
    # connect toSQLite
    con = sqlite3.connect(database_filename)

    data_attacks = [('Malware','Malware uses a vulnerability to breach a network when a user clicks a “planted” dangerous link or email attachment, which is used to install malicious software inside the system.'),
                    ('Phishing','Phishing attacks are extremely common and involve sending mass amounts of fraudulent emails to unsuspecting users, disguised as coming from a reliable source.'),
                    ('Man-in-the-Middle', 'Occurs when an attacker intercepts a two-party transaction, inserting themselves in the middle. From there, cyber attackers can steal and manipulate data by interrupting traffic.'),
                    ('Denial-of-Service', 'DoS attacks work by flooding systems, servers, and/or networks with traffic to overload resources and bandwidth.'),
                    ('SQL Injections', 'This occurs when an attacker inserts malicious code into a server using server query language (SQL) forcing the server to deliver protected information.'),
                    ('Zero-day Exploit', 'Refers to exploiting a network vulnerability when it is new and recently announced ')]

    # Create a connection
    cur = con.cursor()

    # Drop users table if already exists
    cur.execute("DROP TABLE IF EXISTS attacks")

    #Create users table in db_web database
    sql = '''CREATE TABLE "attacks" (
        "attack_id" INTEGER PRIMARY KEY AUTOINCREMENT,
        "name" TEXT,
        "description" TEXT
        )'''

    cur.execute(sql)

    ## Seed the attacks table
    cur.executemany('INSERT INTO attacks(name, description) VALUES (?,?)', data_attacks)

    # Drop users table if already exists
    cur.execute("DROP TABLE IF EXISTS users")

    # Create users table in db_web database
    sql = '''CREATE TABLE "users" (
                "user_id" INTEGER PRIMARY KEY AUTOINCREMENT,
                "username" TEXT,
                "email" TEXT,
                "password" TEXT,
                "phone" INTEGER
                )'''

    cur.execute(sql)

    # commit changes
    con.commit()

    # close the connection
    con.close()

if __name__ == '__main__':
    database_filename = os.environ.get('DATABASE_FILENAME', 'pentracker.db')
    create_db(database_filename)



