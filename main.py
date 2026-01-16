from fastapi import FastAPI
from data import Product
from database import getData, add_data, update_data, delete_data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000"],
                   allow_methods=['*']
)

products = [
    Product(id=1, name="Laptop", description="Dell Laptop", price=150000, quantity=10),
    Product(id=2, name="Laptop", description="Apple Laptop", price=250000, quantity=15),
    Product(id=3, name="Table", description="Computer Table", price=1200, quantity=5),
    Product(id=4, name="Mobile", description="Samsung Galaxy M36", price=22000, quantity=10)
]

# @app.get('/')      # '/' is endpoint here
# def getData5():
#     return "Welcome to home....."

# @app.get('/newPage')
# def newPageData():
#     return "Welcome to new page...."

@app.get('/products')
def get_products():
    return getData()

@app.get('/products/{id}')
def get_products(id:int):
    products = getData()
    for i in products:
        if i.id == id:
            return i
    return "404 Product not Found"

@app.post('/products')
def add_product(product:Product):
    return add_data(product)

@app.put('/products/{id}')
def update_product(id:int, product:Product):
    return update_data(id, product)

@app.delete('/products/{id}')
def delete_product(id:int):
    return delete_data(id)

