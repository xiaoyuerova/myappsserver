from django.urls import path
from specialq import views
from django.urls import include, path
from rest_framework import routers


urlpatterns = [
    path('', views.SpecialSubmitList.as_view()),
    path(r'submit', views.submit),
    path(r'authentic', views.authentic),
]
