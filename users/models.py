from django.contrib.auth.models import AbstractUser
from django_mini_task_manager import settings
from .managers import UserManager
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    image = models.ImageField(upload_to="users_image/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return f"{self.email}"


class UserProfile(models.Model):
    JOB_ROLES = [
        ("programmer", "Програміст"),
        ("manager", "Менеджер"),
        ("analyst", "Аналітик"),
        ("student", "Студент"),
        ("teacher", "Викладач"),
        ("other", "Інше"),
    ]
    USAGE_PURPOSE_CHOICES = [
        ("personal", "Особиста"),
        ("commercial", "Комерційна"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    job_role = models.CharField(max_length=40, choices=JOB_ROLES)
    usage_purpose = models.CharField(max_length=20, choices=USAGE_PURPOSE_CHOICES)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.user.email} profile"
