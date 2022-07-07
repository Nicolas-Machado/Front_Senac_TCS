from typing import Dict
import requests
from siteSenac.service import authenticate, URL_SITE

class SubjectService:

    def get_subjects() -> Dict:
            token = authenticate()
            response = requests.get(f"{URL_SITE}/subject/", headers={'Authorization': 'Token ' + token})  
            if not response.ok:
                return None
            return response.json()

    def get_subject_by_id(subject_id) -> Dict:
            token = authenticate()
            response = requests.get(f"{URL_SITE}/subject/{subject_id}/", headers={'Authorization': 'Token ' + token})  
            if not response.ok:
                return None
            return response.json()

    def post_subject(request, token):
        data = {
                "name" : request['name'],
                "description" : request['description'],
            }
        return requests.post(f"{URL_SITE}/subject/", data=data, headers={'Authorization': 'Token ' + token})

    def put_subject(request, subject_id, token):
        data = {
                "name" : request['name'],
                "description" : request['description'],
            }
        return requests.put(f"{URL_SITE}/subject/{subject_id}/", data=data, headers={'Authorization': 'Token ' + token})
        
    def delete_subject(subject_id, token):
        return requests.delete(f"{URL_SITE}/subject/{subject_id}/", headers={'Authorization': 'Token ' + token})