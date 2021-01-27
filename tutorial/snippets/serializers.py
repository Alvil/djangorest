from rest_framework import serializers

from snippets.models import Snippet
from snippets.models import LANGUAGE_CHOICES
from snippets.models import STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
