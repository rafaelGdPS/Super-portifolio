from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField(max_length=500)

    def __str__(self):
        return self.name
