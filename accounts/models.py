from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    nickname = models.CharField(unique=True, max_length=10)
    point = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
        ]
    )
    level = models.IntegerField(
        default=1,
        validators=[
            MinValueValidator(0),
        ]
    )
    img = models.ImageField(null=True)

