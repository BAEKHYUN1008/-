from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search_law, name='search'),
    path('subscribe/', views.subscribe, name='subscribe'),
]