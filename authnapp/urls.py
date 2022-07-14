from django.urls import path

import authnapp.views as authnapp
from authnapp.apps import AuthnappConfig

app_name = AuthnappConfig.name

urlpatterns = [
    path("login/", authnapp.login, name="login"),
    path("logout/", authnapp.logout, name="logout"),
]
