# users/api/urls.py

from django.urls import path

from .views import (
    RequestRegistrationOtpView,
    RegisterView,
)

urlpatterns = [
    path(
        "request-registration-otp/",
        RequestRegistrationOtpView.as_view(),
    ),

    path(
        "register/",
        RegisterView.as_view(),
    ),
]