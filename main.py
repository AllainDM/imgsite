from fastapi import FastAPI
import uvicorn


app = FastAPI()


# Заглушка БД.
# Список тем.
topics = ["Юмор", "JS", "HTML", "CSS", "Python"]
# Словарь ид картинок по темам(самих картинок нет).
# Создадим словарь с темами(ключ) где значение пустой список.
topics_dict = {i: [] for i in topics}
topics_dict["Юмор"] = [1, 2, 3, 4, 5]
topics_dict["JS"] = [6, 7]
print(f"topics_dict {topics_dict}")


@app.get('/get_topics')
def get_topics():
    # return {i for i in topics}
    return topics


@app.get('/get_topic/{topic}')
def get_topics(topic: str):
    return topics_dict[topic]


@app.get('/get_img/{img_id}')
def get_topics(img_id: int):
    return f"Тут картинка с ид: {img_id}"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
