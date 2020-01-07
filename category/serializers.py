from rest_framework import serializers
from .models import category
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):  # create class to serializer model
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = category
        fields = ('id', 'name', 'status', 'parentId', 'creator')


class UserSerializer(serializers.ModelSerializer):  # create class to serializer usermodel
    category = serializers.PrimaryKeyRelatedField(many=True, queryset=category.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'category')
