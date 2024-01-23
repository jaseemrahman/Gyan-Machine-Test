from django.urls import path, include
from api.views import *

urlpatterns = [

    path('Students',StudentsView.as_view(),name="Students"),

    ]