from django.urls import path
from .views import CreateUser, Login

app_name = "profiles"
urlpatterns = [
    path('register', CreateUser, name="register"),
    path('login', Login, name="login")
]
