from django.contrib import admin
from django.urls import path

import main.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view, name='main_view'),
    path('splash/', views.splash_view, name='splash_view'),
    path('delete', views.delete_view, name='delete_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('user/<str:username>/', views.user_view, name='user_view'),
]
