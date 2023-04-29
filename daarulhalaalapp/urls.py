from django.urls import path
from . import views

app_name = 'daarulhalaalapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.course_registration, name='course_registration'),
    path('about/', views.about_view, name='about'),
]