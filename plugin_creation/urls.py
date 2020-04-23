from django.urls import path

from . import views

urlpatterns = [
	path('', views.create_plugin, name='create_plugin'),
	path(r'^plugin/', views.plugin, name='plugin'),
]