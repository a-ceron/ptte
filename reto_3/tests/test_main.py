import json 
import pytest

from fastapi.testclient import TestClient
from main import app




client = TestClient(app)


def test_get_my_profile():
    """Home response"""
    expect_res = {
        'name': 'Ariel Ceron',
        'age': 26,
        'grade': "M.Sc Science Computing",
        'skills': ['Python', 'FastAPI', 'pyTorch'],
        'experience_years': 8
    }

    response = client.get(
        '/api/v1/'
    )
    res_json = json.loads(response.content.decode('utf-8'))

    assert response.status_code == 200
    assert res_json == expect_res


def test_get_csv_file_success():
    """Return a csv file"""
    payload = {'formato': 'csv'}

    res = client.get(
        'api/v1/ejercicio/descarga',
        params=payload
    )

    assert res.status_code == 200
    assert res.headers['content-type'] == 'text/csv; charset=utf-8'
    assert res.content


def test_get_json_success():
    payload = {'formato': 'json'}

    res = client.get(
        'api/v1/ejercicio/descarga',
        params=payload
    )

    print(res.headers['content-type'])

    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'
    assert res.content


def test_get_file_error():
    with pytest.raises(ValueError, match='Formato no valido'):
        payload = {'formato': 'tsv'}

        res = client.get(
            'api/v1/ejercicio/descarga',
            params=payload
        )

        assert res.status_code == 400
    

def test_post_csv_file_success():
    body = {
        'formato': 'csv'
    }

    res = client.post(
        '/api/v1/ejercicio/descarga',
        json=body
    )

    assert res.status_code == 200
    assert res.headers['content-type'] == 'text/csv; charset=utf-8'
    assert res.content

def test_post_json_success():
    payload = {
        'formato': 'json'
    }

    res = client.post(
        '/api/v1/ejercicio/descarga',
        json=payload
    )

    assert res.status_code == 200
    assert res.headers['content-type'] == 'application/json'
    assert res.content



def test_post_csv_file_body_error():
    with pytest.raises(ValueError, match='Formato no valido'):
        payload = {'formato': 'tsv'}

        res = client.post(
            'api/v1/ejercicio/descarga',
            json=payload
        )

        assert res.status_code == 400
