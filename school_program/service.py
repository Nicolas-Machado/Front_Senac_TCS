from typing import Dict
import requests

from siteSenac.service import authenticate, URL_SITE

class School_ProgramService:

    def get_school_program_by_id(phases_id) -> Dict:
            token = authenticate()
            response = requests.get(f"{URL_SITE}/school_program/{phases_id}/", headers={'Authorization': 'Token ' + token})  
            if not response.ok:
                return None
            return response.json()

    def post_School_Program(request, course, token):
        data = {
                "phase" : request['phase'],
                "phase_time" : request['phase_time'],
                "courses": course,
                "subjects" : request.getlist('subjects'),
            }
        return requests.post(f"{URL_SITE}/school_program/", data=data, headers={'Authorization': 'Token ' + token})

    def put_School_Program(request, phase_id, course, token):
        subjects = request.getlist('subjects')
        subjects = subjects + request.getlist('subjects_add')
        
        data = {
                "phase" : request['phase'],
                "phase_time" : request['phase_time'],
                "courses": course,
                "subjects" : subjects,
            }
        return requests.put(f"{URL_SITE}/school_program/{phase_id}/", data=data, headers={'Authorization': 'Token ' + token})

    def delete_school_program(school_program_id, token):
        return requests.delete(f"{URL_SITE}/school_program/{school_program_id}/", headers={'Authorization': 'Token ' + token})
