from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('evaluate/', views.evaluate, name='evaluate'),
    path('estimate_value/', views.estimate_value, name='estimate_value'),
]