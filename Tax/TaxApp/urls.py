from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:price>/', views.anyNumber, name='anyNumber'),
    path('taxrate/', views.TaxRate, name='TaxRate'),
]