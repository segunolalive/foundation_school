from rest_framework import serializers

from course.models import Chapter, SubChapter

class ChapterSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('heading', 'date_completed')

class SubChapterSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = SubChapter
        fields = ('chapter', 'title', 'text', 'completed_course')
