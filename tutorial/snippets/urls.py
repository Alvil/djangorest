from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import snippet_detail
from .views import SnippetList

urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', snippet_detail, name='snippet-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
