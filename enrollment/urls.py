from .views import *
from django.urls import path

urlpatterns = [

    path('administration/enrollmentList/', enrollmentList, name = 'enrollmentList'),
    path('administration/enrollmentList/enrollmentRegistration', enrollmentRegistration, name = 'enrollmentRegistration'),
    path('administration/enrollmentList/post_enrollment', post_enrollment, name = 'post_enrollment'),
    path('administration/enrollmentList/enrollmentMaintenance', enrollmentMaintenance, name = 'enrollmentMaintenance'),
    path('enrollment_select/', enrollment_select, name = 'enrollment_select'),


]