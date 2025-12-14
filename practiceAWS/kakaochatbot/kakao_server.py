from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "kakaoTest"}


@app.post("/chat/")
def chat(request_data: dict):
    kakaorequest = request_data["userRequest"]["utterance"]

    bot_response = "뭐라는거야"
    if kakaorequest in ["안녕", "반가워", "hi", "hello"]:
        bot_response = "하이! 나 심심해"
    elif kakaorequest.replace(" ", "").replace("?", "").replace("!", "") in ["밥뭐먹을까", "밥뭐먹지"]:
        bot_response = "양갈비!! 당연히 양갈비 먹어야지!!!!!"
    elif kakaorequest == "밥 뭐먹을까?":
        bot_response = "양갈비!! 당연히 양갈비 먹어야지!!!!!"

    return {
        'version': '2.0',
        'template': {
            'outputs': [{"simpleText": {"text": bot_response}}],
            'quickReplies': []
        }
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)