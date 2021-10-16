from mysite.celery import app


@app.task
def add(number1, number2):
    return number1 + number2
