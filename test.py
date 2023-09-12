import psycopg2
# from config import config
connection = psycopg2.connect(
    database="users", 
    user = "tiet", 
    password = "tiet", 
    host = "localhost", 
    port = "5432")

cursor = connection.cursor()
# cursor.execute('''CREATE TABLE USERS
#                     (ID BIGSERIAL PRIMARY KEY,
#                     NAME VARCHAR(100) NOT NULL,
#                     USERNAME VARCHAR(100) UNIQUE NOT NULL,
#                     PASSWORD VARCHAR(100) NOT NULL);''')

cursor.execute("INSERT INTO USERS (NAME, USERNAME, PASSWORD) VALUES ('test', 'test', 'test');")

connection.commit()
connection.close()