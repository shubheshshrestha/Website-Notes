"""
URL configuration for notes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from base.views import home, note_type, create_note, edit_note, create_type, delete_note, register, user_login  # dont use " * " most of the time


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name="home"),
    path('type/', note_type),
    path('create-note/', create_note, name='create-note'),
    path('edit-note/<int:pk>/', edit_note,name='edit-note'),
    path('create-type/', create_type, name='create-type'),
    path('delete-note/<int:pk>/', delete_note, name="delete-note"),
    path("register/", register, name="register"),
    path("login/", user_login, name="login")
]
