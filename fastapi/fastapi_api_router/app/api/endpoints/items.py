from fastapi import APIRouter

router = APIRouter()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@router.get("/")
async def read_item(skip: int = 0, limit: int = 10):
    print(f'skip: {skip}')
    print(f'limit: {limit}')
    return fake_items_db[skip: skip + limit]
