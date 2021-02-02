from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import SnippetDetail
from .views import SnippetList
from .views import UserDetail
from .views import UserList

urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', SnippetDetail.as_view(), name='snippet-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
