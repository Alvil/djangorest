from django.urls import path
from django.urls import include

from rest_framework.routers import DefaultRouter
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.urlpatterns import format_suffix_patterns

from snippets.views import SnippetViewSet
from snippets.views import UserViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
