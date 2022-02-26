from fastapi import Depends, FastAPI
from common import common_parameters

app = FastAPI()


@app.get("/items/")
async def read_items(page: int = 0, commons: dict = Depends(common_parameters)):
    print(page)
    commons[page] = page
    return commons


@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
