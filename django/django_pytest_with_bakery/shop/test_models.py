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
