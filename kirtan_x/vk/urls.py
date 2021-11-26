from django.urls import path
from vk.views import index

urlpatterns = [
    path('vk/', index),
]
