from django.db import models
from django.contrib.auth.models import User


class StudentForm(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    StudentID = models.CharField(blank=False, max_length=10)
    Phone = models.CharField(blank=False, max_length=11)
    Gender = models.CharField(blank=True, null=True, max_length=1)
    
    class Meta:
        verbose_name_plural = "StudentForm"


