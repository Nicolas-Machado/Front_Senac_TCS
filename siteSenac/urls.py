from . import views
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('universities/', views.universities),
    path('university/', views.university),
    path('modalities/', views.modalities),
    path('graduationCourses/', views.graduationCourses),
    path('login/', views.login),

]

