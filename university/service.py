from typing import Dict
import requests

from siteSenac.service import * 


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

    def get_enrollments_university(university_id) -> Dict:
        token = authenticate()
        response = requests.get(f"{URL_SITE}/university/{university_id}/enrollments", headers={'Authorization': 'Token ' + token})  
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
    
    def put_university(request, files, token):
        courses = request.getlist('courses_add')
        courses = courses + request.getlist('courses')
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
                "localization" : request['localization'],
                "is_activate" : request['is_activate'],
                "courses" : courses,
            }

        if 'universityImage' in files:
            img = {
                "university_image_local": files['universityImage']
            }
            return requests.put(f"{URL_SITE}/university/{request['univesity_id']}/", data=data, files=img, headers={'Authorization': 'Token ' + token})
        return requests.put(f"{URL_SITE}/university/{request['univesity_id']}/", data=data, headers={'Authorization': 'Token ' + token})
    
    def post_university(request, files, token):

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
                "localization" : request['localization'],
                "is_activate" : True,
                "courses" : request.getlist('courses'),
            }
        if 'universityImage' in files:
            img = {
                    "university_image_local": files['universityImage']
            }
            return requests.post(f"{URL_SITE}/university/", data=data, files=img, headers={'Authorization': 'Token ' + token})
        return requests.post(f"{URL_SITE}/university/", data=data, headers={'Authorization': 'Token ' + token})


    def put_active_universities(request, token):
        university = requests.get(f"{URL_SITE}/university/{request}/", headers={'Authorization': 'Token ' + token})
        university = university.json()
        
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