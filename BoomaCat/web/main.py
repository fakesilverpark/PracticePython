import uvicorn
from fastapi import FastAPI

from practice.BoomaCat.web import admin, seller, products

app = FastAPI()

app.include_router(admin.router)
app.include_router(seller.router)
app.include_router(products.router)

@app.get("/")
def f():
    return "main"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)