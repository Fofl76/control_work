from django.urls import path
from .views import sgexam_list

urlpatterns = [
    path('sgexam/', sgexam_list, name='sgexam_list'),
] 