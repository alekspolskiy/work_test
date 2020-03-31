from django.db import models


class SomeObjectType(models.Model):
	name = models.CharField(max_length=200, verbose_name='Наименование')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Тип объекта'


class SomeObject(models.Model):
	object_type = models.ForeignKey(SomeObjectType, on_delete=models.CASCADE,verbose_name='Тип объекта')
	description = models.TextField(verbose_name='Описание')

	def __str__(self):
		return self.description

	class Meta:
		verbose_name_plural = 'Объект'
