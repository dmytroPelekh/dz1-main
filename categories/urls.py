from django.urls import path
from . import views

app_name = 'categories'

urlpatterns = [
    path('', views.show_categories, name='show_categories'),
    path('add/', views.add_category, name='add_category'),
    path('edit/<int:pk>/', views.category_edit, name='edit_category'),
    path('delete/<int:pk>/', views.category_delete, name='delete_category'),
]
