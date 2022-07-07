import requests
from datetime import datetime
from siteSenac.service import *


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

    