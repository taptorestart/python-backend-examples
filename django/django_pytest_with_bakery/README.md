# Django bakery example

## Install

Install django and make project and app.

```shell
$ python3 -m venv venv
$ source venv/bin/activate
$ python -m pip install django==3.2.8
$ python -m django startproject mysite .
$ python manage.py startapp shop
```

Install packages
```shell
$ python -m pip install -r requirements.txt
```

## Add app on settings.py
```python
INSTALLED_APPS = [
    ...,
    'shop'
]
```

## Make model
Source: https://github.com/model-bakers/model_bakery

```python
# shop/models.py
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    age = models.IntegerField()

```
Migrate
```shell
$ python manage.py makemigrations
$ python manage.py migrate
```

## pytest.ini
```
[pytest]
DJANGO_SETTINGS_MODULE = mysite.settings
python_files = tests.py test_*.py *_tests.py
addopts = -s
```

## Make test
```python

import pytest
from model_bakery import baker
from shop.models import Customer


@pytest.fixture
def customer():
    """Fixture for baked Customer model."""
    return baker.make(Customer)


@pytest.mark.django_db
def test_using_customer(customer):
    """Test function using fixture of baked model."""
    print(customer.name)
    print(customer.email)
    print(customer.age)
    assert isinstance(customer, Customer)

```

## Run test
```shell
$ pytest
```

Results
```                                                                                                                                                                                                             
....
shop/test_models.py EfUFNbTbNVPozUsFnuLrzTQPHRnnGY
QFPvQWyIhf@example.com
-1218817325
.
======= 1 passed in 0.20s =========
```
