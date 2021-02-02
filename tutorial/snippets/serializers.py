from django.contrib.auth.models import User

from rest_framework import serializers

from snippets.models import Snippet
from snippets.models import LANGUAGE_CHOICES
from snippets.models import STYLE_CHOICES


class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos',
                  'language', 'style', 'owner']


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
