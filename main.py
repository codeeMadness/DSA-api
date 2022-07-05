from fastapi import FastAPI #import class FastAPI() từ thư viện fastapi
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "https://nerd-api.herokuapp.com",
    "http://localhost"
]

app = FastAPI() # gọi constructor và gán vào biến app

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/") # giống flask, khai báo phương thức get và url
async def root(): # do dùng ASGI nên ở đây thêm async, nếu bên thứ 3 không hỗ trợ thì bỏ async đi
    return {"message": "Hello World"}
