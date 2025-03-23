# 전체 라우터 수준에서 의존성 주입하기
from fastapi import Query, HTTPException, FastAPI, Depends


def verify_token(token: str = Query(...)):
    if token != "secureToken":
        raise HTTPException(status_code=401, detail="Invalid token")

app_dep = FastAPI(dependencies=[Depends(verify_token())])
# -> app_dep 사용하는 모든건 다 verify_token 함수를 거친다

@app_dep.get("/public")
def public():
    return {"message": "public endpoint"}

@app_dep.get("/private")
def private():
    return {"message": "private endpoint"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice5_depends:app", reload=True)