from rest_framework import serializers
from .models import Profile, Project, Certificate, CertifyingInstitution


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class NestedCertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["name"]


class CertifyingInstitutionsSerializer(serializers.ModelSerializer):
    certificates = NestedCertificatesSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        certificate_data = validated_data.pop(
            "certificates"
            )
        certifications_institution = CertifyingInstitution.objects.create(
            **validated_data
            )
        for certificate in certificate_data:
            certificate[
                "certifying_institution"
                ] = certifications_institution
            CertificatesSerializer().create(
                validated_data=certificate
                )
        return certifications_institution
