from django.urls import path

from .views import home, detail, new_by_category, add_new, update_new, delete_new, update_category, add_category, delete_category

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:new_id>/', detail, name='detail'),
    path('categories/<int:category_id>/', new_by_category, name='new_by_category'),
    path('news/<int:new_id>/update/', update_new, name='update_new'),
    path('news/<int:new_id>/delete/', delete_new, name='delete_new'),
    path('news/add/', add_new, name='add_new'),
    path('category/add/', add_category, name='add_category'),
    path('category/<int:category_id>/update/', update_category, name='update_category'),
    path('category/<int:category_id>/delete/', delete_category, name='delete_category')
]