
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
    path('IForm/', views.iform, name='iform'),
    path('SForm/', views.sform, name='sform'),
    path('submit_student/', views.submit_student, name='submit_student'),  # Add this line
    path('submit_job/', views.submit_job, name='submit_job'),
    path('clean_data/', views.clean_data, name='clean_data'),
    
]


