# FastAPI oauth2 project example

source: [FastAPI Tutorial - Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/)

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

## screenshots

![POST /token](screenshots/post_token.png)
![GET /users/me](screenshots/get_users_me.png)
![GET /users/me with wrong token](screenshots/get_users_me_with_wrong_token.png)
