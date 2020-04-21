from django.contrib.auth.models import AbstractUser, UserManager
from django.db.models import CharField, EmailField
from django.utils.translation import gettext_lazy as _


class CustomUserManager(UserManager):
    """
    django model manager for user model
    """

    def create_user(self, email=None, password=None, **extra_fields):
        """
        override
        """
        username = email
        return super().create_user(
            username,
            email=email,
            password=password,
            **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        username = email
        return super().create_superuser(
            username,
            email=email,
            password=password,
            **extra_fields
        )


class User(AbstractUser):
    """
    custom user model
    """
    name = CharField(
        max_length=255,
        null=True,
        default=None
    )
    email = EmailField(_('email address'), unique=True)
    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
