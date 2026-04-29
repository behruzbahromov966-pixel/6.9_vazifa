from django.urls import path

from .views import home, detail, new_by_category, add_new

urlpatterns = [
    path('', home, name='home'),
    path('news/<int:new_id>/', detail, name='detail'),
    path('categories/<int:category_id>/', new_by_category, name='new_by_category'),
    path('news/add/', add_new, name='add_new')
]