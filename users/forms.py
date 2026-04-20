from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from users.models import User, UserProfile


class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="Email")
    password = forms.CharField()


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=True)

    job_role = forms.ChoiceField(choices=UserProfile.JOB_ROLES)
    usage_purpose = forms.ChoiceField(choices=UserProfile.USAGE_PURPOSE_CHOICES)

    terms = forms.BooleanField(required=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "terms",
        )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Користувач з таким email вже існує")

        return email

    def clean(self):
        data = super().clean()

        password1 = data.get("password1")
        password2 = data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Паролі не співпадають")

        return data
