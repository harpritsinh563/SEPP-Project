from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    # path('', views.index, name='index'),
    url('addstudentinfo/', views.addstudentinfo),
    url('getstudentinfo/', views.getstudentinfo),
    url('addsuccess/', views.addsuccess),
    url('students/', views.StudentListView.as_view(), name='students'),
]
