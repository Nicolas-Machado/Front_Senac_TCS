from typing import Dict
import requests

from siteSenac.service import *


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

    def post_courses(request, files, token):

        data = {
                "name" : request['name'],
                "course_type" : request['courseType'],
                "course_objective": request['courseObjective'],
                "completion_profile": request['completionProfile'],
                "duration_time": request['durationTime'],
                "occupation_area" : request['occupationArea'],
                "modality" : request['modalities'],
                "mec_score" : request['mecScore'],
                "is_activate" : True
        }
        
        if "curriculum" in files or "courseImage" in files:
            img = {}   
            if "curriculum" in files:
                img.update({"curriculum" : files['curriculum']})
            if "courseImage" in files :
                img.update({"course_image" : files['courseImage']})

            return requests.post(f"{URL_SITE}/course/", data=data, files=img, headers={'Authorization': 'Token ' + token})
        return requests.post(f"{URL_SITE}/course/", data=data, headers={'Authorization': 'Token ' + token})

    def post_courses(request, files, token):

        data = {
                "name" : request['name'],
                "course_type" : request['courseType'],
                "course_objective": request['courseObjective'],
                "completion_profile": request['completionProfile'],
                "duration_time": request['durationTime'],
                "occupation_area" : request['occupationArea'],
                "modality" : request['modalities'],
                "mec_score" : request['mecScore'],
                "is_activate" : True
        }
        
        if "curriculum" in files or "courseImage" in files:
            img = {}   
            if "curriculum" in files:
                img.update({"curriculum" : files['curriculum']})
            if "courseImage" in files :
                img.update({"course_image" : files['courseImage']})

            return requests.post(f"{URL_SITE}/course/", data=data, files=img, headers={'Authorization': 'Token ' + token})
        return requests.post(f"{URL_SITE}/course/", data=data, headers={'Authorization': 'Token ' + token})

    def put_courses(request, files, course_id, token):

        data = {
                "name" : request['name'],
                "course_type" : request['courseType'],
                "course_objective": request['courseObjective'],
                "completion_profile": request['completionProfile'],
                "duration_time": request['durationTime'],
                "occupation_area" : request['occupationArea'],
                "modality" : request['modalities'],
                "is_activate": request['is_activate'],
                "mec_score" : request['mecScore'],
        }
        if "curriculum" in files or "courseImage" in files:
            img = {}   
            if "curriculum" in files:
                img.update({"curriculum" : files['curriculum']})
            if "courseImage" in files :
                img.update({"course_image" : files['courseImage']})

            return requests.put(f"{URL_SITE}/course/{course_id}/", data=data, files=img, headers={'Authorization': 'Token ' + token})
        return requests.put(f"{URL_SITE}/course/{course_id}/", data=data, headers={'Authorization': 'Token ' + token})

    def put_active_courses(request, token):
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
        response = requests.get(f"{URL_SITE}/course/{course_id}/", headers={'Authorization': 'Token ' + token})
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
    