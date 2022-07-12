
from django.contrib import admin
from django.urls import path
from recipies import views
import re

urlpatterns = [
    path("", views.index, name='index'),
    path("login/", views.loginUser, name='login'),  
	path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),
    path("viewdetails/<str:pk>/", views.viewdetails, name='viewdetails'),
    path("search/viewdetails/<str:pk>/", views.viewdetails, name='viewdetails'),
    path("search/editdetails/<str:pk>/", views.editdetails, name='editdetails'),
    path("editdetails/<str:pk>/", views.editdetails, name='editdetails'),
    path("deletedetails/<str:pk>/", views.deldetails, name='deletedetails'),
    path("search/deletedetails/<str:pk>/", views.deldetails, name='deletedetails'),
    path("adddetails/", views.adddetails, name='addetails'),
    path('search/', views.searchBar, name='search'),

]
