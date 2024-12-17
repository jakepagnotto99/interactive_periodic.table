from django.urls import path
from . import views
from .views import ElementCreate, ElementUpdate, ElementDelete

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('elements/', views.elements, name='element_list'),
    path('elements/create/', ElementCreate.as_view(), name='element_create'),
    path('elements/<int:pk>/update/', ElementUpdate.as_view(), name='element_update'),
    path('elements/<int:pk>/delete/', ElementDelete.as_view(), name='element_delete'),
    path('element/<int:element_id>/', views.element_detail, name='element_detail'),
    path('periodic_table/', views.periodic_table, name='periodic_table'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', views.login, name='login'),  
    

]