from django.urls import include
from django.contrib import admin
from django.urls import path

from contact.views import ContactView, ContactDitalsView

urlpatterns = [
    path('tags/', ContactView.as_view(), name='contact'),
    path('tag/<int:pk>', ContactDitalsView.as_view(), name='contact'),
]
