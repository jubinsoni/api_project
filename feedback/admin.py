from django.contrib import admin

# Register your models here.
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id','subject', 'message', 'owner', 'date','image']


admin.site.register(Feedback, FeedbackAdmin)