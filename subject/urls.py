from .views import *
from django.urls import path

urlpatterns = [
    path('', subjectList, name = 'subjectList'),
    path('subjectDelete/<uuid:subject_id>', subjectDelete, name = 'subjectDelete'),
    path('subjectMaintenance/<uuid:subject_id>', subjectMaintenance, name = 'subjectMaintenance'),
    path('administration/courseList/subjectRegistration/', subjectRegistration, name = 'subjectRegistration'),
    path('administration/courseList/post_subject/', post_subject, name = 'post_subject'),
]

