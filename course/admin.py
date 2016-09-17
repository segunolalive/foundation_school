from django.contrib import admin
from .models import Chapter, SubChapter, SubSection

class SubChapterInline(admin.StackedInline):
	model = SubChapter

class SubSectionInline(admin.StackedInline):
	model = SubSection

class ChapterAdmin(admin.ModelAdmin):

	inlines = [SubChapterInline]
	list_display = ('title','slug', 'date_completed',)
	list_filter = ['title', 'date_completed']
	prepopulated_fields = {"slug": ("title",)}
	# search_fields = ['question_text']


class SubChapterAdmin(admin.ModelAdmin):
	list_display = ('title','slug', 'completed',)
	prepopulated_fields = {"slug": ("title",)}


class SubSectionAdmin(admin.ModelAdmin):
	list_display = ('title','slug', 'completed',)
	prepopulated_fields = {"slug": ("title",)}


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(SubChapter, SubChapterAdmin)
admin.site.register(SubSection, SubSectionAdmin)
