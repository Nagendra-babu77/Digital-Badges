from django.db import models

# Create your models here.
class Badge_Details(models.Model):
    Name = models.CharField(max_length=100)  
    Description=models.TextField()
    Image=models.ImageField(upload_to='images/')
    Eligible_students=models.JSONField()
