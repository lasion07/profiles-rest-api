from django.urls import path

from profiles_api import views

"""URL"""
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
