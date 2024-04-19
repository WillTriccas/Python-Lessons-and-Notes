import psycopg2

def create_table():
    connection = psycopg2.connect("dbname = 'First Database' user = 'postgres' password = 'Jasper2009' host = 'localhost' port = '5432'")
    cur = connection.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    connection.commit()
    connection.close()

def insert(item, quantity, price):
    connection = psycopg2.connect("dbname = 'First Database' user = 'postgres' password = 'Jasper2009' host = 'localhost' port = '5432'")
    cur = connection.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quantity, price))
    # cur.execute("INSERT INTO store VALUES('%s','%s','%s')" % (item, quantity, price))     CAN ALSO USE THIS AS A REPLACEMENT TO THE ABOVE BUT IT IS PRONE TO SQL INJECTIONS
    connection.commit()
    connection.close()
 
def view():
    connection = psycopg2.connect("dbname = 'First Database' user = 'postgres' password = 'Jasper2009' host = 'localhost' port = '5432'")
    cur = connection.cursor()
    cur.execute("SELECT * FROM store")
    data_to_show = cur.fetchall()
    connection.close()
    return data_to_show

def delete(item):
    connection = psycopg2.connect("dbname = 'First Database' user = 'postgres' password = 'Jasper2009' host = 'localhost' port = '5432'")
    cur = connection.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    connection.commit()
    connection.close()

def update(quantity, price, item):
    connection = psycopg2.connect("dbname = 'First Database' user = 'postgres' password = 'Jasper2009' host = 'localhost' port = '5432'")
    cur = connection.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    connection.commit()
    connection.close()


update(2000, 0.05, "Grape")


