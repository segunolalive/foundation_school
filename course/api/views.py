from django.db.models import Q


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from course.models import Chapter, SubChapter


from .serializers import (
    ChapterSeriaizer,
    SubChapterSeriaizer,
    )


class ChapterDetailAPIView(RetrieveAPIView):
    queryset = Chapter.objects.all()
    serializer_class = SubChapter
    # lookup_field = 'id'
    permission_classes = [AllowAny]


class ChapterListAPIView(ListAPIView):
    serializer_class = ChapterSeriaizer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title', 'content', 'user__first_name']
    # pagination_class = ChapterPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(ChapterListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Chapter.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(content__icontains=query)|
                    Q(user__first_name__icontains=query) |
                    Q(user__last_name__icontains=query)
                    ).distinct()
        return queryset_list
