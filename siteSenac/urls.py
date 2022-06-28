from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name = 'index'),
    path('universities/', universities, name = 'universities'),
    path('university/<uuid:university_id>/', university, name= 'university'),
    path('modalities/', modalities, name = 'modalities'),
    path('graduationCourses/', graduationCourses, name = 'graduationCourses'),
    path('postGraduateCourses/', postGraduateCourses, name = 'postGraduateCourses'),
    path('courseInfo/ <uuid:course_id>/', courseInfo, name = 'courseInfo'),
    path('login/', login, name = 'login'),
    path('administration/', administration, name = 'administration'),
    path('courseList/', courseList, name = 'courseList'),
    path('courseRegistration/', courseRegistration, name = 'courseRegistration'),
    path('courseMaintenance/', courseMaintenance, name = 'courseMaintenance'),

]

