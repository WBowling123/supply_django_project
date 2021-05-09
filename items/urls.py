from django.urls import path

from . import views


app_name = 'items'
urlpatterns = [
    path('', views.MedicationIndexView.as_view(), name='index'),
]
