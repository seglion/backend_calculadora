import pytest
from app import app

# El cliente de prueba de Flask se configura como una fixture
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_sumar(client):
    response = client.get('/sumar?a=10&b=5')
    assert response.status_code == 200
    assert response.json == {'resultado': 15}

def test_restar(client):
    response = client.get('/restar?a=10&b=5')
    assert response.status_code == 200
    assert response.json == {'resultado': 5}

def test_multiplicar(client):
    response = client.get('/multiplicar?a=10&b=5')
    assert response.status_code == 200
    assert response.json == {'resultado': 50}

def test_dividir(client):
    response = client.get('/dividir?a=10&b=5')
    assert response.status_code == 200
    assert response.json == {'resultado': 2}

def test_dividir_por_cero(client):
    response = client.get('/dividir?a=10&b=0')
    assert response.status_code == 400
    assert response.json == {"error": "División entre cero no permitida"}