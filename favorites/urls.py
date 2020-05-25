from django.urls import path

from . import views


urlpatterns = [
    path('save/', views.favorite_save, name='favorite_save'),
    path('list/', views.favorite_list, name='favorite_list'),
]