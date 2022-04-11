import datetime
import time

from fastapi import FastAPI
import redis
import json

app = FastAPI()
r = redis.Redis(host='localhost', port=6379, db=0)


def get_response(endpoint):
    message = {"message": "Hello World"}
    if r.get(endpoint) is None:
        time.sleep(1)
        r.set(name=endpoint, value=json.dumps(message), ex=datetime.timedelta(seconds=30))
        response = message
    else:
        message = r.get(endpoint).decode('utf-8')
        response = json.loads(message)
    return response


@app.get("/")
async def root():
    endpoint = '/'
    start_time = time.time()
    response = get_response(endpoint)
    process_time = time.time() - start_time
    print(f'process_time: {process_time}')
    return response
