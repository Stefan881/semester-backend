from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_user,name='login_user'),
    path('homepage',views.index,name='index'),
    path('register',views.register_user,name='register'),
    
]