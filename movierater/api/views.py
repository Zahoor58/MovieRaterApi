from django.shortcuts import render
from rest_framework import  viewsets
from .models import Movie, Rating
# Create your views here.
from  . serializers import  MovieSerializer, RatingSerializer
class  MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class  RatingViewSet(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer