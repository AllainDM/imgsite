from fastapi_users import fastapi_users, FastAPIUsers
from pydantic import BaseModel, Field

from fastapi import FastAPI, Request, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.encoders import jsonable_encoder
# from fastapi.exceptions import ValidationError
from fastapi.responses import JSONResponse
import uvicorn

from auth.auth import auth_backend
from auth.database import User
from auth.manager import get_user_manager
from auth.schemas import UserRead, UserCreate

import img_links


app = FastAPI(title="ImgSite")

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()

app.mount("/static", StaticFiles(directory="static"))

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/check_user")
def check_user():
    try:
        user: User = Depends(current_user)
        return f"{user.username}"
    except AttributeError:
        return f"Неавторизованный"


@app.get('/get_topics')
def get_topics():

    # if user:
    #     print(111)
    # else:
    #     print("Пользователь неавторизован.")
    # print(f"Попытка получить картинки: {user.email}")
    # print(f"Попытка получить картинки: {current_user}")
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
