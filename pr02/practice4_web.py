from fastapi import FastAPI

from ch02.data import get_champion

app = FastAPI()

@app.get("/champions")
def all_champions():
    return get_champion()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice4_web:app", reload=True)