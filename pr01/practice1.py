from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get("/hi1")
def greet1():
    return "hello world"
# url: http://127.0.0.1:8000/hi1
# return: hello world
@app.get("/hi2/{who}")
def greet2(who: str):
    return f"{who}, hello world"
# url: http://127.0.0.1:8000/hi2/gaeun
# return: gaeun, hello world

@app.get("/hi3")
def greet3(who):
    return f"{who}, hello world"
# url: http://127.0.0.1:8000/hi3?who=gaeun
# params: key - who, value - gaeun
# return: gaeun, hello world

@app.post("/hi4")
def greet4(who: str = Body(embed = True)):
    return f"{who}, hello world"
# url: http://127.0.0.1:8000/hi4
# body: { "who" : "gaeun" }
# return: gaeun, hello world

@app.get("/hi5")
def greet5(who: str = Header()):
    return f"{who}, hello world"
# url: http://127.0.0.1:8000/hi5
# header:  key - who, value - gaeun
# return: gaeun, hello world

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("practice1:app", reload=True)