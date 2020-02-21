from django.contrib import admin
from basic_app.models import UserProfile, Questions

admin.site.register(Questions)
admin.site.register(UserProfile)
