from django.db import models

# Create your models here.

class teacher(models.Model):
    
    firstname = models.CharField(max_length=240, null=True)
    lastname = models.CharField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    email = models.EmailField(max_length=240, null=True)
    room = models.CharField(max_length=240, null=True)
    subjects = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)  
    

    def __str__(self):
        return self.firstname
    def __str__(self):
        return self.lastname