# FastAPI Form Data project example

source: [FastAPI Tutorial - Form Data](https://fastapi.tiangolo.com/tutorial/request-forms/)

source license: MIT License

## Environments
Python v3.8.2

## Install
```shell
$ mkdir fastapi_minimal
$ cd fastapi_minimal
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ pip install "uvicorn[standard]"
```

## Run
```shell
$ uvicorn main:app --reload
```

Open the login.html and input username and password.
Or use a client program like Postman.

## Screenshots
![Postman POST /login](screenshots/postman_post_login.png)

![Postman log](screenshots/postman_log.png)

![login.html](screenshots/html_login.png)

![login.html Result](screenshots/html_login_result.png)

![login.html log](screenshots/html_login_log.png)
