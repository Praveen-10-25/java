import requests
from bs4 import BeautifulSoup
import mysql.connector

# Step 1: Fetch data from the static site
url = 'https://www.scrapethissite.com/pages/simple/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Step 2: Extract country data
countries_data = soup.find_all('div', class_='country')

# Step 3: Connect to MySQL
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5028"
)
cursor = con.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS webcontent;")
cursor.execute("USE webcontent;")

# Step 4: Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(255),
    capital VARCHAR(255),
    population INT,
    area FLOAT
);
""")

# Step 5: Extract and insert country info
for country in countries_data:
    name = country.find('h3', class_='country-name').get_text(strip=True)
    capital = country.find('span', class_='country-capital').get_text(strip=True)
    population = country.find('span', class_='country-population').get_text(strip=True).replace(',', '')
    area = country.find('span', class_='country-area').get_text(strip=True).replace(',', '')

    try:
        population = int(population)
        area = float(area)
    except ValueError:
        population = 0
        area = 0.0

    cursor.execute("""
        INSERT INTO countries (country_name, capital, population, area)
        VALUES (%s, %s, %s, %s)
    """, (name, capital, population, area))

con.commit()

# Step 6: Fetch and print inserted data
cursor.execute("SELECT * FROM countries;")
for row in cursor.fetchall():
    print(row)

cursor.close()
con.close()

print("✅ Country data inserted and displayed successfully.")
