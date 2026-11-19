from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Ogurtsov API")

class User(BaseModel):
    first_name: str
    last_name: str
    login: str
    email: str
    password: str

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    login: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

@app.get("/users")
async def get_users(limit: Optional[int] = None, page: Optional[int] = None):
    return {
        "users": [],
        "page": page if page is not None else 1,
        "limit": limit if limit is not None else 20
    }

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

@app.post("/user/create_user",
          summary="Создаёт пользователя",
          description="Эндпоинт, который создаёт нового пользователя",
          status_code=200,
          response_model=User)
async def create_user(user: User):
    return user

@app.put("/user/update_user/{user_id}",
         summary="Полное обновление пользователя",
         description="Эндпоинт, который полностью заменяет данные пользователя",
         status_code=200,
         response_model=User)
async def update_user(user_id: int, user: User):
    return user

@app.patch("/user/update_user/{user_id}",
           summary="Частичное обновление пользователя",
           description="Эндпоинт, который частично обновляет данные пользователя",
           status_code=200,
           response_model=UserUpdate)
async def patch_user(user_id: int, user: UserUpdate):
    return user

@app.delete("/user/delete_user/{user_id}",
            summary="Удаление пользователя",
            description="Эндпоинт, который удаляет пользователя по ID",
            status_code=200)
async def delete_user(user_id: int, soft_delete: bool = False):
    return {"user_id": user_id}