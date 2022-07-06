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
    
    #Course Pages (Administration)
    path('administration/courseList/', courseList, name = 'courseList'),
    path('administration/courseList/courseRegistration/', courseRegistration, name = 'courseRegistration'),
    path('administration/courseList/schoolProgramRegistration/', schoolProgramRegistration, name = 'schoolProgramRegistration'),
    path('administration/courseList/subjectRegistration/', subjectRegistration, name = 'subjectRegistration'),
    path('administration/courseDetails/<uuid:course_id>/', courseDetails, name = 'courseDetails'),

    #University Pages (Administration)
    path('administration/courseMaintenance/<uuid:course_id>/', courseMaintenance, name = 'courseMaintenance'),
    path('administration/universityList/', universityList, name = 'universityList'),
    path('administration/universityRegistration/', universityRegistration, name = 'universityRegistration'),
    path('administration/universityMaintenance/<uuid:university_id>/', universityMaintenance, name = 'universityMaintenance'),
]

