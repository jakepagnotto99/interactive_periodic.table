from django.contrib import admin
from django.urls import path, include
from periodic_table import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('',include('periodic_table.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
