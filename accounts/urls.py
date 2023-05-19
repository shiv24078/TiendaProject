from django.urls import path
from .views import register
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('password_change/', views.change_password, name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
]
