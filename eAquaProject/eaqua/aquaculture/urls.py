from django.urls import path
from . import views

urlpatterns = [
    path('diseases/', views.disease_list, name='disease_list'),
    path('manage/diseases/', views.manage_diseases, name='manage_diseases'),
    path('manage/diseases/add/', views.add_disease, name='add_disease'),
    path('manage/diseases/edit/<int:pk>/',
         views.edit_disease, name='edit_disease'),
    path('manage/diseases/delete/<int:pk>/',
         views.delete_disease, name='delete_disease'),

]
