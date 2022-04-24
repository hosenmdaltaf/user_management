from django.urls import path

from . import views

app_name="account"

urlpatterns = [
    path('home/', views.homepage, name='homepage'),
    path('', views.loginview, name='loginpage'),
    path('logout/', views.logout, name='logoutpage'),
    path('register/', views.register, name='registerpage'),
    path('password_reset/', views.password_reset, name='password_resetpage'),
    path('register_edit/', views.register_edit, name='register_editpage'),
]
 