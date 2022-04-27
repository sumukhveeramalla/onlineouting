from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name = 'home'),
    path('login',views.login,name = 'login'),
    path('logout',views.logout,name = 'logout'),
    path('adminlogin', views.adminlogin, name = 'adminlogin'),
    path('actual',views.actual,name='actual'),
    path('display',views.display,name='display')
]