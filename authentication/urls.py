from django.urls import path, include
from . import views
from authentication.views import *

urlpatterns = [

    path('Login',LoginView.as_view(),name="Login"),

    ]