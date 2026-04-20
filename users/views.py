from django.utils.http import url_has_allowed_host_and_scheme
from users.forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetDoneView,
)
from django.views.generic import FormView
from django.contrib import auth, messages
from users.services import UserService
from django.urls import reverse_lazy
from users.dto import CreateUserDTO


class UserLoginView(LoginView):
    template_name = "users/login.html"
    form_class = UserLoginForm

    def get_success_url(self):
        redirect_to = self.request.POST.get("next") or self.request.GET.get("next")

        if redirect_to and url_has_allowed_host_and_scheme(
            url=redirect_to,
            allowed_hosts={self.request.get_host()},
        ):
            return redirect_to

        return reverse_lazy("core:home")

    def form_valid(self, form):
        messages.success(
            self.request, f"{form.get_user().first_name}, Вас було авторизовано."
        )

        return super().form_valid(form)


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        data = form.cleaned_data

        user = UserService().register_user(
            CreateUserDTO(
                first_name=data["first_name"],
                last_name=data.get("last_name"),
                email=data["email"],
                password=data["password1"],
                job_role=data["job_role"],
                usage_purpose=data["usage_purpose"],
                terms=data["terms"],
            )
        )

        auth.login(self.request, user)

        messages.success(self.request, "Акаунт успішно створено!")

        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    pass


class CustomPasswordResetConfirmView(PasswordResetDoneView):
    pass
