from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from clientbase.apps import ClientbaseConfig
from clientbase.views import CustomUserCreateView, email_verification

app_name = ClientbaseConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(next_page="clientbase:login"), name="logout"),
    path("register/", CustomUserCreateView.as_view(), name="register"),
    path("email-confirm/<str:token>/", email_verification, name="email-confirm")
]
