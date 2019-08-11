from rest_framework.serializers import ModelSerializer

from topics.models import Topic, Celebrity


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = [
            'id',
            'name',
            'image'
        ]


class CelebritySerializer(ModelSerializer):
    class Meta:
        model = Celebrity
        fields = [
            'id',
            'name',
            'image'
        ]
