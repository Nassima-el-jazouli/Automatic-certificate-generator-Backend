from django.db import models

# Create your models here.
class Certificate(models.Model):
    Type = models.CharField(max_length=60, blank=False, default='')
    Title = models.CharField(max_length=70, blank=False, default='')
    Description = models.CharField(max_length=250, blank=False, default='')
    Date = models.DateField(blank=False)
    Image = models.FileField(upload_to ='uploads/images/', max_length=254, blank=False)
    File = models.FileField(upload_to ='uploads/files/', max_length=254, blank=False)