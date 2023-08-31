from django.db import models


class GeneratedResponse(models.Model):
    content = models.TextField()
    file_name = models.CharField(max_length=255)

    def __str__(self):
        return self.file_name


class GeneratedImage(models.Model):
    description = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return self.description
