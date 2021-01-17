from django.db import models

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField('authentication.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    dob = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username