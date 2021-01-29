from django.http import Http404

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(ListCreateAPIView):
    """
    List all code snippets, or create a new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
