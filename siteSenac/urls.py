from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name = 'index'),
    path('universities/', universities, name = 'universities'),
    path('university/<uuid:university_id>/', university, name= 'university'),
    path('modalities/', modalities, name = 'modalities'),
    path('services/', services, name = 'services'),
    path('courses_results/', courses_results, name = 'courses_results'),
    path('graduationCourses/', graduationCourses, name = 'graduationCourses'),
    path('postGraduateCourses/', postGraduateCourses, name = 'postGraduateCourses'),
    path('courseInfo/<uuid:course_id>/', courseInfo, name = 'courseInfo'),
    path('login/', login, name = 'login'),
    path('administration/', administration, name = 'administration'),
    path('login_authentication/', login_authentication, name = 'login_authentication'),
    path('courseList/', courseList, name = 'courseList'),
    path('universityList/', universityList, name = 'universityList'),
    path('courseRegistration/', courseRegistration, name = 'courseRegistration'),
    path('courseSave/', courseSave, name = 'courseSave'),
    path('universityRegistration/', universityRegistration, name = 'universityRegistration'),
    path('courseMaintenance/<uuid:course_id>/', courseMaintenance, name = 'courseMaintenance'),
    path('universityMaintenance/<uuid:university_id>/', universityMaintenance, name = 'universityMaintenance'),
    path('schoolProgramRegistration/', schoolProgramRegistration, name = 'schoolProgramRegistration'),
]

