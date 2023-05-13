from specialq import views
from django.urls import include, path, re_path
from rest_framework import routers


urlpatterns = [
    re_path(r'^specialsubmit/$', views.SpecialSubmitList.as_view()),
    path(r'specialsubmit/<int:id>/', views.SpecialSubmitDetail.as_view()),

    path('', views.SpecialSubmitList.as_view()),
    path(r'submit', views.submit),
    path(r'authentic', views.authentic),
    path('admin/<str:opt>', views.SpecialSubmitManege.as_view()),
]
