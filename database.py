import mysql.connector as sql
from data import Product

conn = sql.connect(host='localhost', user='root', password='root')
conn.autocommit = True
cur = conn.cursor()
cur.execute("use data;")

def getData():
    products = []
    cur.execute("select * from fastdata;")
    data = cur.fetchall()
    for i in data:
        products.append(Product(id=i[0], name=i[1], description=i[2], price=i[3], quantity=i[4]))
    return products

def add_data(product:Product):
    query = f"insert into fastdata values \
        ({product.id}, '{product.name}', '{product.description}', {product.price}, {product.quantity});"
    cur.execute(query)
    return "record added successfully"

def update_data(id:int, product:Product):
    query = f"update fastdata set \
        name = '{product.name}', description = '{product.description}', price = {product.price}, quantity = {product.quantity} \
            where id = {id}"
    cur.execute(query)
    return "record updated successfully"

def delete_data(id:int):
    query = f"delete from fastdata where id = {id}"
    cur.execute(query)
    return "record deleted successfully"