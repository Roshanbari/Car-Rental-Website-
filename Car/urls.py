from django.contrib import admin
from django.urls import path,include
from Car import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('book/',views.book,name='book')

]