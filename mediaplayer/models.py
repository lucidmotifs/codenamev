from django.db import models


# Create your models here.

class Genre(models.Model):
	genre_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date created')


class Video(models.Model):
	video_name = models.CharField(max_length=200)
	video_rating = models.IntegerField(default=3)
	video_desc = models.CharField(max_length=255)
	genre = models.ForeignKey(Genre)
	pub_date = models.DateTimeField('data published')