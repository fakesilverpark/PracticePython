from fastapi import FastAPI, Query, Depends

app = FastAPI()

# 1. 유저 조회 후 의존성 리턴
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice5_depends:app", reload=True)