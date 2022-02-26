# FastAPI Request Body project example

source: [FastAPI Tutorial - Request Body](https://fastapi.tiangolo.com/tutorial/body/)

source license: MIT License

## Environments
Python v3.8.2

## Install
```shell
$ mkdir fastapi_minimal
$ cd fastapi_minimal
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install "uvicorn[standard]"
$ pip install -r requirements.txt
```

## Run
```shell
$ uvicorn main:app --reload
```

## Screenshots

Read the body of the request as JSON

![POST /items](screenshots/post_items_with_json_body.png)

![Log](screenshots/post_items_log.png)
