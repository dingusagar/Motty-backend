from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from topics.models import Topic, Celebrity
from topics.serializers import TopicSerializer, CelebritySerializer


class TopicViewSet(viewsets.ModelViewSet):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()


class CelebrityViewSet(viewsets.ModelViewSet):
    serializer_class = CelebritySerializer
    queryset = Celebrity.objects.all()
