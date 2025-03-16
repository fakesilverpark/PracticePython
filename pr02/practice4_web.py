from fastapi import FastAPI

from practice.pr02.practice4_data import get_all_champions, get_champion

app = FastAPI()

@app.get("/champions")
def all_champions():
    return get_all_champions()

@app.get("/champions/{champion_id}")
def champion(champion_id: int):
    return get_champion(champion_id)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice4_web:app", reload=True)