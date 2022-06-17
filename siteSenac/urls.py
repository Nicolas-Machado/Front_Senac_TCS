from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name = 'index'),
    path('universities/', universities, name = 'universities'),
    path('university/', university, name= 'university'),
    path('modalities/', modalities, name = 'modalities'),
    path('graduationCourses/', graduationCourses, name = 'graduationCourses'),
    path('postGraduateCourses/', postGraduateCourses, name = 'postGraduateCourses'),
    path('login/', login, name = 'login'),
    path('administration/', administration, name = 'administration'),

]

