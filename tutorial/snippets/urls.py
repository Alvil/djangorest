from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import api_root
from snippets.views import SnippetDetail
from snippets.views import SnippetList
from snippets.views import UserDetail
from snippets.views import UserList

urlpatterns = [
    path('', api_root, name='api-root'),
    path('snippets/', SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
