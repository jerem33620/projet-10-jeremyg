from django.urls import path

from . import views


urlpatterns = [
    path('research/', views.research, name='research'),
    path('info/<int:code>/', views.product_info, name='product_info')
]