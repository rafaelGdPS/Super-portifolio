from django.shortcuts import render

from projects.serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertificatesSerializer,
    CertifyingInstitutionsSerializer
    )
from .models import Profile, Project, Certificate, CertifyingInstitution
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            profile_id = kwargs.get("pk")
            profile = Profile.objects.get(id=profile_id)
            context = {"profile": profile}
            return render(request, "profile_detail.html", context)

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionsViewSet(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionsSerializer


class CertificatesViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificatesSerializer
