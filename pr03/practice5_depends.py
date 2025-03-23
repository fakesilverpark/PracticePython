from fastapi import FastAPI, Query, Depends, HTTPException

app = FastAPI()

# 1. 유저 조회 후 의존성 리턴
def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender}

@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user

# 2. 토큰 확인 후 권한 부여
def check_admin(token: str = Query(...)):
    if token == "secureToken":
        return {"role": "admin"}
    raise HTTPException(status_code=401, detail="invalid token")

@app.get("/check_admin")
def check_admin(user: dict = Depends(check_admin)):
    return {"message" : "welcome", "user": user}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice5_depends:app", reload=True)