from django.db import models
from django.utils import timezone
from django.urls import reverse


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

	def get_absolute_url(self):
		return reverse("course:detail", kwargs={"slug":self.sub_chapter.slug, "slug2":self.slug, "pk":self.sub_chapter.chapter.pk,
		})

