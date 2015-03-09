from django.db import models

class Book(models.Model):
	pub_date = models.DateField()
	title = models.CharField(max_length=200)
	field_of_study = models.CharField(max_length=1, 
		choices = (
			("C","C"),
			("J","Java"),
			("H","PHP"),
			("P","Python")
			))
