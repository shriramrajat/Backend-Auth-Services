
from fastapi import FastAPI
from models import Products

app=FastAPI()

@app.get("/")
def greet():
      return "Hello World" 

products=[
     Products(id=1,name="Phone",description="Budget Phone",price=999,quantity=50),
     Products(id=2,name="Laptop",description="Gaming Laptop",price=4999,quantity=30),
     Products(id=3,name="Tablet",description="Smart Tablet",price=799,quantity=60),
     Products(id=4,name="Headphones",description="Wireless Headphones",price=199,quantity=80)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
      for product in products:
           if product.id==product_id:
                  return products[product_id-1]
           
      return {"message":"Product not found"}

@app.post("/products")
def add_new_product(new_product:Products):
      products.append(new_product)
      return new_product


