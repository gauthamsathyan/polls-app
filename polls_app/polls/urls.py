from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('create_poll/', views.create_poll, name='create_poll'),
]