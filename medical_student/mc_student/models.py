from django.db import models

# Create your models here.
class Medical_Civil(models.Model):
    CHOICES =(
    ("Medical", "Medical"),
    ("Civil", "Civil Engineering"),
)
    name=models.CharField(max_length=255)
    college_name=models.CharField(max_length=255)
    batch=models.CharField(max_length=255,choices=CHOICES)
    cotact=models.BigIntegerField()
    mail=models.EmailField()