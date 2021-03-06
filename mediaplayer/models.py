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
	title = models.CharField(max_length=50)
	show = models.ForeignKey(Show)
	season = models.ForeignKey(Season)	
	rating = models.IntegerField()

	def __unicode__(self):
		return "{}: Season {:d}, Episode {:d} - {}".format(self.show.name, self.season.number, self.number, self.title)


class Channel(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=255)
	created = models.DateTimeField('Date Created')
	modified = models.DateTimeField('Date Modified')

	def __unicode__(self):
		return self.name


class Video(models.Model):
	title = models.CharField(max_length=200)
	filename = models.FileField()
	rating = models.IntegerField(default=3)
	desc = models.CharField(max_length=255)
	genre = models.ForeignKey(Genre)
	creator = models.ForeignKey(Creator)
	pub_date = models.DateTimeField('data published')

	def __unicode__(self):
		return self.title


class Comment(models.Model):
	text = models.TextField()
	votes = models.IntegerField(default=0)
	video = models.ForeignKey(Video)
	created = models.DateTimeField('Created')
	modified = models.DateTimeField('Modified')