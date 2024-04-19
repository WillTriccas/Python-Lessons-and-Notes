import sqlite3

def create_table():
    connection = sqlite3.connect("Example.db")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = sqlite3.connect("Example.db")
    cur = connection.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    connection.commit()
    connection.close()
 
def view():
    connection = sqlite3.connect("Example.db")
    cur = connection.cursor()
    cur.execute("SELECT * FROM store")
    data_to_show = cur.fetchall()
    connection.close()
    return data_to_show

def delete(item):
    connection = sqlite3.connect("Example.db")
    cur = connection.cursor()
    cur.execute("DELETE FROM store WHERE item = ?", (item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = sqlite3.connect("Example.db")
    cur = connection.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    connection.commit()
    connection.close()
 
##update(40, 10.25, "Dog Bowl")
#print(view())

#create_table()
#insert("Champagne Flute", 82, 7.50)
#insert("Wine Glass", 15, 5)
#insert("Beer tankard",22, 12.75)
#insert("Dog Bowl", 2, 20)
#delete("Champagne Flute")


#change the above  lines each time you execute the data - otherwise you will keep inputting the same data to the table each time 
#and create duplicates

