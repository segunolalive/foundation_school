from django.contrib import admin
from .models import Chapter, SubChapter

class SubChapterInline(admin.TabularInline):
	model = SubChapter


class ChapterAdmin (admin.ModelAdmin):
	# fieldsets = [
	# (None, {'fields': ['question_text']}),
	# ('Date Info', {'fields': ['pub_date'], 'classes': ['collapse']}),
	# ]
	inlines = [SubChapterInline]
	list_display = ('title', 'date_completed',)
	list_filter = ['title', 'date_completed']
	prepopulated_fields = {"slug": ("title",)}
	# search_fields = ['question_text']


admin.site.register(Chapter, ChapterAdmin)
