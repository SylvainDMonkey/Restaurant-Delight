from django.urls import path

from . import views

app_name="inventory"
urlpatterns = [
    path("home", views.home, name="home"),
    path("login", views.login_view, name="login"),
]