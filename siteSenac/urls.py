from .views import *
from django.urls import path

urlpatterns = [
    # User Side Paths
    path('', index, name = 'index'),
    path('modalities/', modalities, name = 'modalities'),
    path('services/', services, name = 'services'),
    path('contact/', contact, name = 'contact'),

    # Administration Paths
    path('logout/', logout, name = 'logout'),
    path('login/', login, name = 'login'),
    path('administration/', administration, name = 'administration'),
    path('administration_home/', administration_home, name = 'administration_home'),
]

