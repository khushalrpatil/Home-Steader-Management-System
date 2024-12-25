from django.urls import path
from . import views

urlpatterns = [
    path("", views.all, name="all"),
    path("register", views.register),
    path("login", views.login),
    path("logout/", views.logout),
    path("request_training", views.request_training),
    path("<str:name>/", views.info),
    path("delete/<int:id>/", views.delete),
]
