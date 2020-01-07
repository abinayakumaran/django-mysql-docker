from rest_framework import serializers
from .models import News
from django.contrib.auth.models import User


class NewsSerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = News
        fields = ('id', 'name', 'image_url', 'status', 'tracking_id', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    news = serializers.PrimaryKeyRelatedField(many=True, queryset=News.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'news')
