# from django.shortcuts import render

from projects.serializers import ProfileSerializer
from .models import Profile
from rest_framework import viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
