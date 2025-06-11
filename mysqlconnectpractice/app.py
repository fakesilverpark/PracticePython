import uvicorn
from fastapi import FastAPI

from practice.mysqlconnectpractice.database import cur

app = FastAPI()

@app.get("/")
def f():
    cur.execute("select * from users")
    return cur.fetchall()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
