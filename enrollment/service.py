import requests
from datetime import datetime
from course.service import CourseService
from siteSenac.service import *
from university.service import UniversityService


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
    
    def search_date_enrollment_activate(courses, university_id) -> Dict:
        _list = []
        for course in courses:
            for enrollment in course['enrollments']:
                if enrollment['date_final'] >= datetime.today().strftime('%Y-%m-%d'):
                    if university_id != None:
                        if enrollment['universities'] == university_id:
                            _list.append(course)  
                            break
                    else:
                        _list.append(course)
                        break

            
        return _list

    def search_date_enrollment_university_activate(universities, course_id) -> Dict:
        _list = []
        for university in universities:
            response = UniversityService.get_enrollments_university(university['id'])
            for enrollment in response:
                courses = CourseService.get_courses_by_id(course_id)
                if courses['enrollments'] == enrollment:
                    print(university['name'])
                    break

        
        return _list
    
    def post_enrollment(request, token):
        data = {
                "date_initial" : request['date_initial'],
                "date_final" : request['date_final'],
                "courses" : request['course_enrollment'],
                "universities" : request['university']
            }
        return requests.post(f"{URL_SITE}/enrollment/", data=data, headers={'Authorization': 'Token ' + token})

    