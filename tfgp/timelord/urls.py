from django.conf.urls import url
from timelord import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^timetable/$', views.timetable, name='timetable'),
    url(r'^createtask/$', views.create_task, name='create_task'),
    url(r'^timetable/edittask/$', views.edit_task, name='edit_task'),
    url(r'^timetable/editcategories/$', views.edit_categories, name='edit_categories'),
    url(r'^account/$', views.account, name='account'),
    url(r'^logout/$', views.user_logout, name='logout'),
]
