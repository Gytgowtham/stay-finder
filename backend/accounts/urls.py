from django.urls import path
from .views import login_page, signup_page, home, select_area

urlpatterns = [
    path("", login_page),
    path("signup/", signup_page),
    path("home/", home),
    path("select-area/", select_area),
]
