from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Genre(models.Model):
	genre_name = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date created')

	def __unicode__(self):
		return self.genre_name
		

class Creator(models.Model):
	name = models.CharField(max_length=50)
	pseudo = models.CharField(max_length=50)
	registered = models.DateTimeField('Date Registered')
	avatar = models.ImageField()
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.pseudo


class Studio(models.Model):
	name = models.CharField(max_length=50)
	icon = models.ImageField()
	creator = models.ForeignKey(Creator)

	def __unicode__(self):
		return self.name


class Show(models.Model):
	name = models.CharField(max_length=50)
	genre = models.ForeignKey(Genre)
	rating = models.IntegerField()
	creator = models.ForeignKey(Creator)
	studio = models.ForeignKey(Studio)
	created = models.DateTimeField('Date Created')

	def __unicode__(self):
		return self.name


class Season(models.Model):
	number = models.IntegerField()
	show = models.ForeignKey(Show)

	def __unicode__(self):
		return "Season %d" % self.number


class Episode(models.Model):
	number = models.IntegerField()
	season = models.ForeignKey(Season)
	show = models.ForeignKey(Show)
	rating = models.IntegerField()


class Channel(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	created = models.DateTimeField('Date Created')
	modified = models.DateTimeField('Date Modified')


class Video(models.Model):
	video_name = models.CharField(max_length=200)
	video_rating = models.IntegerField(default=3)
	video_desc = models.CharField(max_length=255)
	genre = models.ForeignKey(Genre)
	pub_date = models.DateTimeField('data published')

	def __unicode__(self):
		return self.video_name