import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '943dca9d601da1f9703bfcf92353ba62'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
TRAINER_ID = '38143'


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_trainer_name():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Oozzz163'  



@pytest.mark.parametrize('key, value', [('trainer_name', 'Oozzz163'), ('id', TRAINER_ID)])
def test_parametriize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})  
    assert response_parametrize.json()["data"][0][key] == value