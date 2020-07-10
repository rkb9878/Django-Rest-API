from rest_framework import serializers
from profiles_api.models import snippet
from profiles_api import models

class helloSerializer(serializers.Serializer):
    """Serializers serialize a name field for testing our ApiView"""
    name=serializers.CharField(max_length=10)
    mobile=serializers.CharField(max_length=15)

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer a user profile object"""
    class Meta:
        model=models.User_Profile

        fields=('id','email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self, validated_data):
        """Create and return new users"""
        user=models.User_Profile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user






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

class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializers profile feed items"""

    class Meta:
        model=models.ProfileFeedItem
        fields=[
            'id',
            'user_profile',
            'status_text',
            'created_on'
        ]

        extra_kwargs={
            'user_profile':{'read_only':True}
        }





