from .views import *
from django.urls import path

urlpatterns = [
    path('', universities, name = 'universities'),
    path('<uuid:university_id>/', university, name= 'university'),
    path('administration/universityList/', universityList, name = 'universityList'),
    path('administration/universityRegistration/', universityRegistration, name = 'universityRegistration'),
    path('administration/post_university/', post_university, name = 'post_university'),
    path('administration/universityMaintenance/<uuid:university_id>/', universityMaintenance, name = 'universityMaintenance'),
    path('administration/put_university/', put_university, name = 'put_university'),

]

