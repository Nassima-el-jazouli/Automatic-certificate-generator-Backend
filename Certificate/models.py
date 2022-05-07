from django.db import models

# Create your models here.
class Certificate(models.Model):
    Type = models.CharField(max_length=60, blank=False, default='')
    Title = models.CharField(max_length=70, blank=False, default='')
    Description = models.CharField(max_length=250, blank=False, default='')
    Date = models.DateField(blank=False)
    myImage = models.FileField(upload_to ='media/myImages/', max_length=254, blank=False)
    myFile = models.FileField(upload_to ='media/myFiles/', max_length=254, blank=False)

    def __str__(self):
        return self.name