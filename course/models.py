from django.db import models
from django.utils import timezone


class Chapter(models.Model):
	heading = models.CharField(max_length=200)
	date_completed = models.DateTimeField(blank=True, null=True)
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.heading


class SubChapter(models.Model):
	chapter = models.ForeignKey(Chapter)
	title = models.CharField(max_length=200)
	text = models.TextField()
	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title
