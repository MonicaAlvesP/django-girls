from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list, name='post_list'),
  path('sala',views.sala),
  path('sala2',views.sala2),
]