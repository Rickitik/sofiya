from django.shortcuts import render
from django.views.generic.base import View
from .models import Child


class ChildView(View):
	"""Список детей"""
	def get(self, request):
		children = Child.objects.all()
		return render(request, 'child_list.html', {'child_list': children})


class ChildDetailView(View):
	"""Описание ребенка"""
	def get(self, request, slug):
		child = Child.objects.get(url=slug)
		return render(request, 'child_detail.html', {'child': child})
