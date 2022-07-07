import requests
from siteSenac.service import authenticate, URL_SITE
from university.service import UniversityService

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
                "courses": request['course'],
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