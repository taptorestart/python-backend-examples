# FastAPI Dependencies First Steps project example
Source: [Dependencies - First Steps](https://fastapi.tiangolo.com/tutorial/dependencies) 

## Environments
Python v3.8.2

## Install
```shell
$ mkdir fastapi_dependencies_first_steps
$ cd fastapi_dependencies_first_steps
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install fastapi==0.74.1
$ pip install "uvicorn[standard]"
```

## Run
```shell
$ uvicorn main:app --reload
```

## Screenshots
![GET /items](screenshots/get_items.png)

![GET /users](screenshots/get_users.png)
