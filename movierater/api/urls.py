
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from . views import MovieViewSet, RatingViewSet,UserViewSet
router=routers.DefaultRouter()
router.register('movies',MovieViewSet)
router.register('users',UserViewSet)
router.register('ratings',RatingViewSet)


urlpatterns = [
    path('', include(router.urls) ),
   
]
