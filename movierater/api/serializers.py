from pyexpat import model
from tokenize import Token
from  rest_framework import serializers
from django.contrib.auth.models import User
from .models import Movie,Rating
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id', 'username', 'password')
        extra_kwargs={'password': {'write_only':True,'required':True}}
    # our own create user method
    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=('id', 'title', 'description','no_of_ratings','avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields=('id', 'stars', 'user','movie',)