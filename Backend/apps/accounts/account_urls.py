from django.urls import path

from .account_views import (
    AccountSignupView,
    AccountLoginView,
    AccountProfileView
)


urlpatterns = [

    path(
        "signup/",
        AccountSignupView.as_view(),
        name="account-signup"
    ),

    path(
        "login/",
        AccountLoginView.as_view(),
        name="account-login"
    ),

    path(
        "profile/",
        AccountProfileView.as_view(),
        name="account-profile"
    ),

]