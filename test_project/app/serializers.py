from rest_framework.serializers import ModelSerializer
from .models import SomeObject, SomeObjectType
from rest_framework import serializers


class SomeObjectViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = SomeObject
		fields = ('description', 'object_type')


class SomeObjectTypeViewSerializer(serializers.ModelSerializer):
	class Meta:
		model = SomeObjectType
		fields = ['name']



class SomeObjectSerializer(serializers.ModelSerializer):
	class Meta:
		#user = serializers.HiddenField(default=serializers.CurrentUserDefault())
		model = SomeObject
		fields = '__all__'


class SomeObjectTypeSerializer(serializers.ModelSerializer):
	class Meta:
		model = SomeObjectType
		fields = '__all__'


