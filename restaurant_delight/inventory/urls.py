from django.urls import path

from . import views

app_name="inventory"
urlpatterns = [
    path("", views.login_view, name="login"),
    path("home", views.home, name="home"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.sign_up_view, name="signup"),
]