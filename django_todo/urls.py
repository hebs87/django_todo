"""django_todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_auth import views as auth_views
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Authentication
    path('register/', auth_views.registeruser, name='registeruser'),
    path('login/', auth_views.loginuser, name='loginuser'),
    path('logout/', auth_views.logoutuser, name='logoutuser'),

    # To-Do
    path('', todo_views.home, name='home'),
    path('current/', todo_views.currenttodos, name='currenttodos'),
    path('create/', todo_views.createtodo, name='createtodo'),
    path('edit/<int:todo_id>', todo_views.edittodo, name='edittodo'),
]
