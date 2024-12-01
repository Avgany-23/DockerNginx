from rest_framework.test import APIClient
from api.models import Product
import pytest


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_url(api_client):
    response = api_client.get('http://89.111.169.119:80/api/v1/stocks/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_url_redirect(api_client):
    response = api_client.get('http://89.111.169.119:80/api/v1/stocks')
    assert response.status_code == 301


@pytest.mark.django_db
def test_access_create_product(api_client):
    json_data = {
        'title': 'test title',
    }

    response = api_client.post(
        path='http://89.111.169.119:80/api/v1/products/',
        data=json_data
    )

    assert response.status_code == 201
    assert response.json()['title'] == json_data['title']
    assert response.json()['description'] is None


@pytest.mark.django_db
def test_failure_create_product(api_client):
    json_data = {
        'title': 'test title',
    }
    Product(title=json_data['title']).save()

    response = api_client.post(
        path='http://89.111.169.119:80/api/v1/products/',
        data=json_data
    )

    assert response.status_code == 400
