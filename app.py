from flask import Flask, render_template, flash
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "5028",
    "database": "webcontent"
}

@app.route("/")
def home():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM countries;")
        dip = cursor.fetchall()
    except mysql.connector.Error as err:
        flash(f"Database Error: {err}", "danger")
        dip = []
    finally:
        cursor.close()
        connection.close()
    return render_template('home.html', values=dip)

if __name__ == "__main__":
    app.run(debug=True)
