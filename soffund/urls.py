from django.urls import path
from . import views

urlpatterns = [
	path('', views.ChildView.as_view()),
	path('<slug:slug>/', views.ChildDetailView.as_view(), name='child_detail')
]
