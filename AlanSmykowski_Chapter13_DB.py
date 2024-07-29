#This program creates a population database and simulates population growth

import sqlite3
import matplotlib.pyplot as plt


#Function to create database
def createDatabaseAndTable():

    #Connect to SQLite
    conn = sqlite3.connect('population_AS.db')
    cursor = conn.cursor()

    #Create table
    cursor.execute('''CREATE TABLE IF NOT EXISTS population
                      (city TEXT, year INTEGER, population INTEGER)''')

    #Commit and close connection
    conn.commit()
    conn.close()


#Function to insert initial data
def insertInitialData():

    #List of cities in FL
    cities = ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee', 
              'Fort Lauderdale', 'Naples', 'Sarasota', 'Pensacola', 'St. Augustine']
    initial_population = [470914, 309154, 397085, 954614, 197102, 
                          182437, 199000, 57645, 54300, 154671]

    #Connect to SQLite
    conn = sqlite3.connect('population_AS.db')
    cursor = conn.cursor()

    #Insert data
    for i in range(len(cities)):
        cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                       (cities[i], 2023, initial_population[i]))

    #Commit and close connection
    conn.commit()
    conn.close()


#Function to simulate population growth
def simulatePopulationGrowth():

    growth_rate = 0.02

    #Connect to SQLite database
    conn = sqlite3.connect('population_AS.db')
    cursor = conn.cursor()

    #Retrieve initial data
    cursor.execute("SELECT city, population FROM population WHERE year = 2023")
    rows = cursor.fetchall()

    #Simulate growth
    for row in rows:
        city, population = row
        for year in range(2024, 2044):
            population = int(population * (1 + growth_rate))
            cursor.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                           (city, year, population))

    #Commit and close connection
    conn.commit()
    conn.close()


#Function to display population growth for a city
def showPopulationGrowth():

    #List of cities
    cities = ['Miami', 'Orlando', 'Tampa', 'Jacksonville', 'Tallahassee', 
              'Fort Lauderdale', 'Naples', 'Sarasota', 'Pensacola', 'St. Augustine']

    #Display options
    print("Choose a city to display population growth:")
    for i, city in enumerate(cities):
        print(f"{i + 1}. {city}")

    #Get user choice
    choice = int(input("Enter the number corresponding to the city: "))
    selected_city = cities[choice - 1]

    #Connect to SQLite
    conn = sqlite3.connect('population_AS.db')
    cursor = conn.cursor()

    #Retrieve data
    cursor.execute("SELECT year, population FROM population WHERE city = ?", (selected_city,))
    rows = cursor.fetchall()

    #Separate data
    years = [row[0] for row in rows]
    populations = [row[1] for row in rows]

    #Plot data
    plt.plot(years, populations, marker='o')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.show()

    #Close connection
    conn.close()


#Main
def main():

    #Create database
    createDatabaseAndTable()

    #Insert data
    insertInitialData()

    #Simulate growth
    simulatePopulationGrowth()

    #Show population growth for a city
    showPopulationGrowth()


#Main call
if __name__ == "__main__":
    main()
