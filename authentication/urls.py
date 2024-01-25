from django.urls import path, include
from . import views
from authentication.views import *

urlpatterns = [
    path('Registration',RegistrationApiView.as_view(),name="Registration"),
    path('Login',LoginApiView.as_view(),name="Login"),

    ]