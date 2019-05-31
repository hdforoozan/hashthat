from django.db import models

class Hash(models.Model):
	text = models.TextField()
	Hash = models.CharField(max_length=64)
