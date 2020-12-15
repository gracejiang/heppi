from django.contrib import admin
from django.urls import path

import main.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main_view')
]
