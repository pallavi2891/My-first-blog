from django.db import models
from django.utils import timezone



class Song(models.Model):
    songname=models.CharField(max_length=1000)
    singer=models.CharField(max_length=200)
    created_date=models.DateTimeField(default=timezone.now)
    lyrics=models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

class User(models.Model):
	name=models.CharField(max_length=200)
	Gender=models.CharField(max_length=20)
	specialized_in=models.CharField(max_length=200)

	def __str__(self):
		return self.name 
	
	

