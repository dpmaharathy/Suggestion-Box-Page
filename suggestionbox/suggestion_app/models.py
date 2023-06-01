from django.db import models

# Create your models here.

class Suggestion(models.Model):
    employee_id = models.CharField(max_length=100)
    suggestion = models.TextField()
    resolution = models.TextField()
