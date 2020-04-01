from django.contrib import admin
from django.urls import path
from app import views
from app.views import *


app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('objects/create/', SomeObjectCreateView.as_view()),
    path('objects/all/', SomeObjectListView.as_view()),
    path('object_types/create/', SomeObjectTypeCreateView.as_view()),
    path('object_types/all/', SomeObjectTypeListView.as_view()),
    path('objects/detail/<int:pk>/', ObjectsDetailView.as_view()),
    path('object_types/detail/<int:pk>/', ObjectsTypeDetailView.as_view()),
]
