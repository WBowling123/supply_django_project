from django.urls import path

from . import views


app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('meds/<int:med_id>', views.med_detail_view, name='medication detail'),
]
