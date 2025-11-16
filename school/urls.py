from django.urls import path
from . import views

urlpatterns = [
    path('add-items/', views.add_items, name='add_items'),
]
