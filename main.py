
from fastapi import FastAPI, HTTPException, status
from models import Product

app=FastAPI()

@app.get("/")
def greet():
      return "Hello World" 

products=[
     Product(id=1,name="Phone",description="Budget Phone",price=999,quantity=50),
     Product(id=2,name="Laptop",description="Gaming Laptop",price=4999,quantity=30),
     Product(id=3,name="Tablet",description="Smart Tablet",price=799,quantity=60),
     Product(id=4,name="Headphones",description="Wireless Headphones",price=199,quantity=80)
]

@app.get("/products")
def get_all_products():
    return products

@app.get("/product")
def get_product_by_id(product_id: int):
      for product in products:
           if product.id==product_id:
                  return product
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.post("/product", status_code=status.HTTP_201_CREATED)
def add_new_product(new_product:Product):
      products.append(new_product)
      return new_product

@app.put("/product")
def update_product(product_id:int,new_product:Product):
      for i in range(len(products)):
            if products[i].id == product_id:
                  products[i]=new_product
                  return {"message":f"Product with id {product_id} updated successfully"}
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")

@app.delete("/product", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id:int):
      for i in range(len(products)):
            if products[i].id == product_id:
                  del products[i]
                  return
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")



