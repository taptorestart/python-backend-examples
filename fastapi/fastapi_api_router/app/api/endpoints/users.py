from fastapi import APIRouter

router = APIRouter()

fake_name_db = [{"user_name": "John"}, {"user_name": "Ted"}, {"user_name": "James"}]


@router.get("/")
async def read_user(skip: int = 0, limit: int = 10):
    print(f'skip: {skip}')
    print(f'limit: {limit}')
    return fake_name_db[skip: skip + limit]
