from django.contrib.auth import get_user_model
from users.dto import CreateUserDTO
from users.models import UserProfile
from django.db import transaction


class UserService:
    def __init__(self):
        self.model = get_user_model()

    @transaction.atomic
    def register_user(self, user_data: CreateUserDTO):
        user = self.model.objects.create_user(
            email=user_data.email,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            password=user_data.password,
        )

        UserProfile.objects.create(
            user=user,
            job_role=user_data.job_role,
            usage_purpose=user_data.usage_purpose,
            phone_number=user_data.phone_number,
        )
        return user
