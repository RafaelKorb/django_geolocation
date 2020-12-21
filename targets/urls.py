
from django.urls import path
from .views import list_targets, create_target, update_target, delete_target, show_map

urlpatterns = [
    path('', list_targets, name='list_targets'),
    path('map', show_map, name='show_map'),
    path('new', create_target, name='create_targets'),
    path('update/<int:id>/', update_target, name='update_target'),
    path('delete/<int:id>/', delete_target, name='delete_target'),
]