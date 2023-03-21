from . import views
from django.urls import path
app_name ='collegeapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('allcourse',views.allcourse,name='allcourse'),
    path('regform',views.regform,name='regform'),
    path('get-course/',views.get_course,name="get_course"),

]