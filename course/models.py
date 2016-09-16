from django.db import models
from django.utils import timezone


class Chapter(models.Model):
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(unique=True)
	date_completed = models.DateTimeField(blank=True, null=True)

	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class SubChapter(models.Model):
	chapter = models.ForeignKey(Chapter)
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(unique=True)

	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title


class SubSection(models.Model):
	sub_chapter = models.ForeignKey(SubChapter)
	title = models.CharField(max_length=200, unique=True)
	slug = models.SlugField(unique=True)
	text = models.TextField(null=True, blank=False)

	completed = models.BooleanField(default=False)

	def __str__(self):
		return self.title
