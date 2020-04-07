from django.urls import path

from . import views

urlpatterns = [
    path("", views.appsearch, name="app_search"),
    path("ajax/", views.ajaxsearch, name="ajax"),
]
