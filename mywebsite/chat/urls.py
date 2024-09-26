from django.urls import path
from . import views

urlpatterns = [
	path('', views.lobby)
	# path('', views.lobby, name='lobby'), 
]