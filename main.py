from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
import uvicorn


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Заглушка БД.
# Список тем.
topics = ["Юмор", "JS", "HTML", "CSS", "Python"]
# Словарь ид картинок по темам(самих картинок нет).
# Создадим словарь с темами(ключ) где значение пустой список.
topics_dict = {i: [] for i in topics}
topics_dict["Юмор"] = [1, 2, 3, 4, 5]
topics_dict["JS"] = [6, 7]
topics_dict["CSS"] = [15, 17]
print(f"topics_dict {topics_dict}")
# Словарь с изображениями, где ключ id, а значение путь
dict_img = {}
dict_img[1] = '1.jpg'
print(f"dict_img {dict_img}")


@app.get('/get_topics')
def get_topics():
    # return {i for i in topics}
    return topics


@app.get('/get_topic/{topic}')
def get_topics(topic: str):
    return topics_dict[topic]


@app.get('/get_img/{img_id}')
def get_topics(img_id: int):
    return f"img/{dict_img[img_id]}"


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
