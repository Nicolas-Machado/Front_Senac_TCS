from .views import *
from django.urls import path

urlpatterns = [
    # User Side Paths
    path('', index, name = 'index'),
    path('universities/', universities, name = 'universities'),
    path('universities/university/<uuid:university_id>/', university, name= 'university'),
    path('modalities/', modalities, name = 'modalities'),
    path('services/', services, name = 'services'),
    path('contact/', contact, name = 'contact'),
    path('courses_results/', courses_results, name = 'courses_results'),
    path('modalities/graduationCourses/', graduationCourses, name = 'graduationCourses'),
    path('modalities/postGraduateCourses/', postGraduateCourses, name = 'postGraduateCourses'),
    path('courseInfo/<uuid:course_id>/', courseInfo, name = 'courseInfo'),

    # Administration Paths
    path('login/', login, name = 'login'),
    path('administration/', administration, name = 'administration'),
    path('login_authentication/', login_authentication, name = 'login_authentication'),
    
    #Course Pages (Administration)
    path('administration/courseList/', courseList, name = 'courseList'),
    path('administration/courseList/courseRegistration/', courseRegistration, name = 'courseRegistration'),
    path('courseSave/', courseSave, name = 'courseSave'),
    path('administration/courseList/schoolProgramRegistration/', schoolProgramRegistration, name = 'schoolProgramRegistration'),

    #University Pages (Administration)
    path('administration/courseMaintenance/<uuid:course_id>/', courseMaintenance, name = 'courseMaintenance'),
    path('administration/universityList/', universityList, name = 'universityList'),
    path('administration/universityRegistration/', universityRegistration, name = 'universityRegistration'),
    path('administration/universityMaintenance/<uuid:university_id>/', universityMaintenance, name = 'universityMaintenance'),
]

