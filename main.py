from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import uvicorn

import img_links


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/get_topics')
def get_topics():
    return img_links.topics


@app.get('/get_topic/{topic}')
def get_topics(topic: str):
    try:
        return img_links.dict_img[topic]
    except KeyError:
        return "Неверный ключ"


# @app.get('/get_img/{img_id}')
# def get_topics(img_id: int):
#     return f"static/img/{dict_img[img_id]}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
