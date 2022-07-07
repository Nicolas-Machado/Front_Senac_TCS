from .views import *
from django.urls import path

urlpatterns = [
    path('school_ProgramDelete/<uuid:school_program_id>', school_ProgramDelete, name = 'school_ProgramDelete'),
    path('administration/courseList/schoolProgramRegistration/<uuid:course_id>', schoolProgramRegistration, name = 'schoolProgramRegistration'),
    path('administration/courseList/schoolProgramMaintenance/<uuid:phases_id>', schoolProgramMaintenance, name = 'schoolProgramMaintenance'),

]
