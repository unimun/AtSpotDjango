from django.forms import widgets
from rest_framework import serializers
from .models import Profile
from drf_extra_fields.fields import Base64ImageField

class ProfileSerializer(serializers.ModelSerializer):
    img = Base64ImageField(represent_in_base64=True)
    class Meta:
        model = Profile
        fields = ('user', 'nickname', 'point', 'img',)
    