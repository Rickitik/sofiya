from django.db import models
from django.urls import reverse
from datetime import time, date


class Category(models.Model):
	"""Категория"""
	name = models.CharField('Категория', max_length=20)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'


class Child(models.Model):
	"""Дети"""
	name = models.CharField('Имя', max_length=12)
	surname = models.CharField('Фамилия', max_length=20)
	lastname = models.CharField('Отчество', max_length=20)
	birthday = models.DateField('Дата рождения')
	diagnos = models.TextField('Диагноз')
	photo = models.ImageField('Изображение', upload_to='main_photo/')
	url = models.SlugField(max_length=130, unique=True)
	money = models.PositiveSmallIntegerField('Необходимая сумма')
	category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
	pay_date = models.DateField('Дата оплаты')
	pay_description = models.TextField('Описание оплаты', help_text='Иванову С. было оплачено лечение')
	full_name = models.CharField('ФИО в дательном падеже', max_length=150)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('child_detail', kwargs={'slug': self.url})

	class Meta:
		verbose_name = 'Ребенок'
		verbose_name_plural = 'Дети'


class Documents(models.Model):
	"""Сканы документов детей"""
	child = models.ForeignKey(Child, verbose_name='Документы ребенка', on_delete=models.CASCADE)
	document_image = models.ImageField('Сканы документов', upload_to='document_image/children/')

	def __str__(self):
		return f'Документы {self.child.name}'

	class Meta:
		verbose_name = 'Документы ребенка'
		verbose_name_plural = 'Документы детей'


class FundDocuments(models.Model):
	"""Документы фонда"""
	name = models.CharField('Наименование документа фонда', max_length=50)
	description = models.TextField('Описание документа фонда')
	document_image = models.FileField('Файл для скачивания', upload_to='document_image/fund/')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Документ для скачивания'
		verbose_name_plural = 'Документы для скачивания'

