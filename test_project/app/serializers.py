from rest_framework.serializers import ModelSerializer
from .models import SomeObject, SomeObjectType

class SomeObjectSerializer(ModelSerializer):
	class Meta:
		model = SomeObject
		fields = '__all__'


class SomeObjectTypeSerializer(ModelSerializer):
	class Meta:
		model = SomeObjectType
		fields = '__all__'
