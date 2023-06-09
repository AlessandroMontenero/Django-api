from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('dishes/', views.dishes_list),
    path('dishes/<int:pk>/', views.dish_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
