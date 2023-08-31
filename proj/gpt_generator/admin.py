from django.contrib import admin

from .models import GeneratedImage, GeneratedResponse


admin.site.register(GeneratedResponse)
admin.site.register(GeneratedImage)
