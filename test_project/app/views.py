from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import SomeObject, SomeObjectType
from .serializers import SomeObjectTypeSerializer, SomeObjectSerializer


def home(request):

	list_objects = SomeObject.objects.all()
	list_object_types = SomeObjectType.objects.all()

	context = {
		'list_objects': list_objects,
		'list_object_types': list_object_types
	}

	template = 'index.html'

	return render(request, template, context)


class SomeObjectCreateView(ModelViewSet):
	serializer_class = SomeObjectSerializer


class SomeObjectTypeCreateView(ModelViewSet):
	serializer_class = SomeObjectTypeSerializer	


class SomeObjectListView(ModelViewSet):
	queryset = SomeObject.objects.all()
	serializer_class = SomeObjectSerializer
	

class SomeObjectTypeListView(ModelViewSet):
	queryset = SomeObjectType.objects.all()
	serializer_class = SomeObjectTypeSerializer	
	