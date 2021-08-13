from django.urls import path

from . import views

app_name = 'users'
urlpatterns = [
    path('', views.ListUsers.as_view(), name='listusers'),
    path('register/', views.CreateUser.as_view(), name='createuser')
]
