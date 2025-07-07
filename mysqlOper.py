import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="5028"
)
cursor=con.cursor()
cursor.execute("""create database IF NOT EXISTS employeeDb;""")
cursor.execute("""use employeeDb;""")
table = """
CREATE TABLE my_table (
    id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(200)NOT NULL,
    mail_id VARCHAR(200) NOT NULL,
    ph_number varchar(10) NOT NULL
)
"""
cursor.execute(table)
cursor.execute("""desc my_table;""")
for row in cursor:
    print(row)
print("db created Successfully")
cursor.close()