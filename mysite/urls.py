from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('',views.index,name='index'),
    #path('login',views.login),
    path('notes/',views.notes,name='notes'),
    path('logout/',views.user_logout,name='logout'),
    path('updateprofile/',views.updateprofile),
    path('about/',views.about),
    path('contact/',views.contact),
]
