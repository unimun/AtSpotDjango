from django.shortcuts import render

from .models import Profile

from .serializers import ProfileSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import detail_route

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)