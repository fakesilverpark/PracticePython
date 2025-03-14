from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get("/hi1")
def greet1():
    return "hello world"

@app.get("/hi2/{who}")
def greet2(who: str):
    return f"{who}, hello world"

@app.get("/hi3")
def greet3(who):
    return f"{who}, hello world"

@app.get("/hi4")
def greet4(who: str = Body(embed = True)):
    return f"{who}, hello world"

@app.get("/hi5")
def greet5(who: str = Header()):
    return f"{who}, hello world"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)