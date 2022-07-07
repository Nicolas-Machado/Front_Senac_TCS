from typing import Dict
import requests

URL_SITE = 'http://127.0.0.1:7000'


def authenticate() -> Dict:
    login = {'username': 'admin', 'password': 'admin'}
    response = requests.post(f"{URL_SITE}/rest-auth-token/", data=login)
    token = response.json()['token']
    return token

def adm_authenticate(username, password) -> Dict:
    login = {'username': username, 'password': password}
    response = requests.post(f"{URL_SITE}/rest-auth-token/", data=login)
    if response.status_code != 400:
        token = response.json()['token']
        return token
    return None




    


