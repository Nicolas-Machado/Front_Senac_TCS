from typing import Dict
from urllib import request
import requests
import json

URL_SITE = 'http://127.0.0.1:7000'

def authenticate() -> Dict:
        login = {'username': 'nicolas', 'password': 'Nic1234@'}
        response = requests.post(f"{URL_SITE}/rest-auth-token/", data=login)
        token = response.json()['token']
        return token

class UniversityService():

    def get_universities() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/?is_activate=true", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json()

    def get_universities_by_id(university_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/{university_id}", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()
    
    def get_universities_by_name(name) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/?search={name}&is_activate=true", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()
    
    def get_courses_in_university(university_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/{university_id}/courses/?is_activate=true", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()   

class CourseService():

    def get_courses() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/?is_activate=true", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json()

    def get_courses_by_name(name) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/?search={name}&is_activate=true", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()

    def get_courses_by_id(course_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/{course_id}/?is_activate=true", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()   

    def get_universities_in_course(course_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/{course_id}/universities/?is_activate=true", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()

class EnrollmentService():

    def get_enrollments() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/enrollment/", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json()
    
    def get_courses_enrollments(enrollment_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/enrollment/{enrollment_id}/courses/", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json()
    


