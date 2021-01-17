from django.contrib import admin

# Register your models here.
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'bio', 'dob']


admin.site.register(UserProfile, UserProfileAdmin)