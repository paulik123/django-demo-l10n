from django.db import models

# Create your models here.
class Demo(models.Model):
	name = models.CharField(max_length=255)
	some_datetime = models.DateTimeField()