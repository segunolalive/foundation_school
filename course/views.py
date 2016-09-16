from django.shortcuts import render
from django.utils import timezone
from .models import Chapter, SubChapter
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect

def chapter_list(request):
	chapters = Chapter.objects.all()
	return render(request, 'cefs/chapter_list.html', {'chapters':chapters})


def subchapter_list(request, pk):
	chapter = get_object_or_404(Chapter, pk=pk)
	subchapters = chapter.subchapter_set.all()
	return render(request, 'cefs/subchapter_list.html', {'subchapters':subchapters})

def subsection_list(request, slug):
	sub_chapter = get_object_or_404(SubChapter, slug=slug)
	sub_sections = sub_chapter.sub_section_set.all()
	return render(request, 'cefs/sub_section_list.html', {'sub_sections:sub_sections'})

# edit this to determine how subsections are queried and published
def detail(request, pk):
	course = get_object_or_404(SubChapter, pk=pk)
	return render(request, 'cefs/detail.html', {'course':course})
