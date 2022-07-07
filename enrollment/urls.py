from .views import *
from django.urls import path

urlpatterns = [

    path('administration/enrollmentList/', enrollmentList, name = 'enrollmentList'),
    path('administration/enrollmentList/enrollmentRegistration', enrollmentRegistration, name = 'enrollmentRegistration'),


]