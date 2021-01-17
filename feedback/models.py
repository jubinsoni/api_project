from django.db import models
from authentication.models import User
from PIL import Image


# Create your models here.


class Feedback(models.Model):

    subject = models.CharField(max_length=250)
    message = models.TextField()
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    image = models.ImageField(default='default.jpg', upload_to='feedback_pics')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # To execute save() method from parent class

        img = Image.open(self.image.path)

        if(img.height > 300 or img.width > 300):
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
