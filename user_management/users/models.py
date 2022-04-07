from django.db import models

# Create your models here.
class UserDocument(models.Model):
    description = models.CharField(max_length=255, blank=True)
    documet = models.FileField(upload_to='media/')