from django.urls import path, reverse_lazy
from users import views
from django.contrib.auth.views import LogoutView

app_name = "users"
urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("register/", views.UserRegisterView.as_view(), name="register"),
    path("reset-password/", views.PasswordResetView.as_view(), name="reset_password"),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name="reset_password",
    ),
    path(
        "logout/",
        LogoutView.as_view(
            next_page=reverse_lazy("core:landing_page"),
        ),
        name="logout",
    ),
]
