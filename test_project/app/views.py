from django.shortcuts import render
from .models import SomeObject, SomeObjectType
from .serializers import SomeObjectTypeSerializer, SomeObjectSerializer, SomeObjectViewSerializer,SomeObjectTypeViewSerializer
from rest_framework import generics, permissions 



def home(request):

	list_objects = SomeObject.objects.all()
	list_object_types = SomeObjectType.objects.all()

	context = {
		'list_objects': list_objects,
		'list_object_types': list_object_types
	}

	template = 'index.html'

	return render(request, template, context)



class SomeObjectCreateView(generics.CreateAPIView):
	#permissions_classes = [permissions.AllowAny]
	serializer_class = SomeObjectSerializer


class SomeObjectTypeCreateView(generics.CreateAPIView):
	#permissions_classes = [permissions.AllowAny]
	serializer_class = SomeObjectTypeSerializer	


class SomeObjectListView(generics.ListAPIView):
	#permissions_classes = [permissions.AllowAny]
	queryset = SomeObject.objects.all()
	serializer_class = SomeObjectViewSerializer
	

class SomeObjectTypeListView(generics.ListAPIView):
	#permissions_classes = [permissions.AllowAny]
	queryset = SomeObjectType.objects.all()
	serializer_class = SomeObjectTypeViewSerializer	
	

class ObjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
	#permissions_classes = [permissions.AllowAny]
	serializer_class = SomeObjectSerializer
	queryset = SomeObject.objects.all()


class ObjectsTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
	#permissions_classes = [permissions.AllowAny]
	serializer_class = SomeObjectTypeSerializer
	queryset = SomeObjectType.objects.all()

