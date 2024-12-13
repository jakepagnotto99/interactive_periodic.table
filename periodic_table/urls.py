from django.urls import path
from . import views
from .views import ElementCreate, ElementUpdate, ElementDelete

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('elements/', views.elements, name='element_list'),
    path('elements/create/', ElementCreate.as_view(), name='element_create'),
    path('elements/<int:pk>/update/', ElementUpdate.as_view(), name='element_update'),
    path('elements/<int:pk>/delete/', ElementDelete.as_view(), name='element_delete'),
    path('element/<int:element_id>/', views.element_detail, name='element_detail'),
]
