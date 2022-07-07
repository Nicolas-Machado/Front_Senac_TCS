from .views import *
from django.urls import path

urlpatterns = [
    # User Side Paths
    path('courses_results/', courses_results, name = 'courses_results'),
    path('modalities/graduationCourses/', graduationCourses, name = 'graduationCourses'),
    path('modalities/postGraduateCourses/', postGraduateCourses, name = 'postGraduateCourses'),
    path('courseInfo/<uuid:course_id>/', courseInfo, name = 'courseInfo'),
    path('administration/courseList/', courseList, name = 'courseList'),
    path('administration/courseList/courseRegistration/', courseRegistration, name = 'courseRegistration'),
    path('administration/courseDetails/<uuid:course_id>/', courseDetails, name = 'courseDetails'),
    path('administration/courseMaintenance/<uuid:course_id>/', courseMaintenance, name = 'courseMaintenance'),


]

