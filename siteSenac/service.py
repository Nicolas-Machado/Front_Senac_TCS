import json
from typing import Dict
from datetime import datetime
import requests

URL_SITE = 'http://127.0.0.1:7000'

def authenticate() -> Dict:
    login = {'username': 'nicolas', 'password': 'Nic1234@'}
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


class UniversityService():

    def get_universities() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/?is_activate=true", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json()

    def get_all_universities() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/", headers={'Authorization': 'Token ' + token})  
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
    
    def post_university(request):
        token = authenticate()
        print(request)
        for courses in request['courses']:
            print(courses)

            data = {
                    "name" : request['name'],
                    "telephone" : request['phone'],
                    "phone_number": request['optionalPhone'],
                    "attendance" : request['attendance'],
                    "email": request['emailUniversity'],
                    "street": request['street'],
                    "neighborhood" : request['neighborhood'],
                    "city" : request['city'],
                    "state" : request['state'],
                    "zip_code" : request['zipCode'],
                    "house_number" : request['houseNumber'],
                    "university_image_local" : request['universityImage'],
                    "is_activate" : True,
                    "courses" : courses['id'],
                }
        return requests.post(f"{URL_SITE}/university/", data=data, headers={'Authorization': 'Token ' + token})

    def put_active_universities(request, token):
        token = authenticate()
        university = requests.get(f"{URL_SITE}/university/{request}/", headers={'Authorization': 'Token ' + token})
        university = university.json()
        
        for courses in university['courses']:
            if(university['is_activate'] == False):
                university['is_activate'] = True
            else:
                university['is_activate'] = False
            data = {
                "name" : university['name'],
                "telephone" : university['telephone'],
                "phone_number": university['phone_number'],
                "city" : university['city'],
                "zip_code" : university['zip_code'],
                "house_number" : university['house_number'],
                "is_activate" : university['is_activate'],
            }

        return requests.patch(f"{URL_SITE}/university/{request}/", data=data, headers={'Authorization': 'Token ' + token})
    

class CourseService():

    def get_courses_in_university(university_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/{university_id}/courses/?is_activate=true", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()   
    
    def get_courses_in_university_by_name(university_id, name) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/{university_id}/courses/?search={name}&is_activate=true", headers={'Authorization': 'Token ' + token})
        if not response.ok:
            return None
        return response.json()  

    def get_all_courses() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json()

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

    def put_active_courses(request, token):
        token = authenticate()
        course = requests.get(f"{URL_SITE}/course/{request}/", headers={'Authorization': 'Token ' + token})
        course = course.json()
        if(course['is_activate'] == False):
            course['is_activate'] = True
        else:
            course['is_activate'] = False
        data = {
            "name" : course['name'],
            "duration_time": course['duration_time'],
            "occupation_area" : course['occupation_area'],
            "is_activate" : course['is_activate']
        }
       
        return requests.patch(f"{URL_SITE}/course/{request}/", data=data, headers={'Authorization': 'Token ' + token})

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

    def get_courses_graduation() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/?course_type=GRADUACAO&is_activate=true", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json() 

    def get_courses_graduation_by_name(name) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/?search={name}&course_type=GRADUACAO&is_activate=true", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json()  

    def get_courses_postgraduation() -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/?course_type=POS_GRADUACAO&is_activate=true", headers={'Authorization': 'Token ' + token})  
        if not response.ok:
            return None
        return response.json() 

    def get_courses_postgraduation_by_name(name) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/course/?search={name}&course_type=POS_GRADUACAO&is_activate=true", headers={'Authorization': 'Token ' + token})  
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
    
    def get_subjects_in_phases(school_program_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}school_program/{school_program_id}/subjects/", headers={'Authorization': 'Token ' + token})  
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
    
    def search_date_enrollment_activate(courses) -> Dict:
        _lista = []
        for course in courses:
            for enrollment in course['enrollments']:
                if enrollment['date_final'] >= datetime.today().strftime('%Y-%m-%d'):
                    _lista.append(course)
        
        return _lista

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
    


