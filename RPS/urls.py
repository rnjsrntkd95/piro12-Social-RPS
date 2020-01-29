from django.urls import path

from RPS import views

app_name = 'RPS'

urlpatterns = [
    path('', views.home, name='home'),
    path('log/<int:pk>/', views.log, name='log'),
    path('attack/<int:pk>/', views.attack, name='attack'),
    path('defense/<int:log_pk>/<int:pk>', views.defense, name='defense'),
]