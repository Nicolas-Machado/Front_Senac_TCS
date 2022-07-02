from lib2to3.pgen2 import token
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

    def post_courses(request, files):
        token = authenticate()

        print(files['curriculum'])

        data = {
                "name" : request['name'],
                "course_type" : request['courseType'],
                "course_objective": request['courseObjective'],
                "curriculum" : files['curriculum'],
                "completion_profile": request['completionProfile'],
                "duration_time": request['durationTime'],
                "occupation_area" : request['occupationArea'],
                "modality" : request['modalities'],
                "course_image" : files['courseImage'],
                "mec_score" : request['mecScore'],
        }
        return requests.post(f"{URL_SITE}/course/", data=data, headers={'Authorization': 'Token ' + token})

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

    def get_phases_in_courses(course_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/{course_id}/school_programs", headers={'Authorization': 'Token ' + token})  
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

class Send_EmailService():

    def post_send_email(request):
        token = authenticate()
        university = UniversityService.get_universities_by_id(request['universities'])
        if "course" in request:
            data = {
                "name" : request['name'],
                "email" : request['email'],
                "email_university": university['email'],
                "phone_number" : request['phone_number'],
                "message": request['message'],
                "courses": request['courses'],
                "universities" : request['universities']
            }
        else:
            data = {
                "name" : request['name'],
                "email" : request['email'],
                "email_university": university['email'],
                "phone_number" : request['phone_number'],
                "message": request['message'],
                "universities" : request['universities']
            }
        return requests.post(f"{URL_SITE}/send_email/", data=data, headers={'Authorization': 'Token ' + token})
    


