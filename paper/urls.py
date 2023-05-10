from django.urls import path
from paper import views
from django.urls import include, path
from rest_framework import routers


urlpatterns = [
    path('', views.PaperList.as_view()),
    path('<int:uid>', views.PaperDetail.as_view()),
    path('admin/<str:opt>', views.PaperManege.as_view()),
]
