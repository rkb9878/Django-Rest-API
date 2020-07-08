from rest_framework import serializers
from profiles_api.models import snippet

class helloSerializer(serializers.Serializer):
    """Serializers serialize a name field for testing our ApiView"""
    name=serializers.CharField(max_length=10)
    mobile=serializers.CharField(max_length=15)

class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(max_length=200)
    linenos = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return snippet.objects.create(**validated_data)



