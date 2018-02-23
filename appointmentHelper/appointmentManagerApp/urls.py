from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index', ),
    path('getAppointment/<str:search_string>/', views.getAppointment, name='getAppointment'),
]