from django.urls import path

from RPS import views

app_name = 'RPS'

urlpatterns = [
    path('', views.main, name='main'),
    path('log/<int:pk>/', views.log, name='log'),
    path('attack/<int:pk>/', views.attack, name='attack'),
    path('defense/<int:log_pk>/<int:pk>', views.defense, name='defense'),
    path('lobby/', views.offline_log, name='offline_log'),
    path('offline_play/', views.offline_play, name='offline_play'),
    path('cpu_status/<int:pk>/', views.cpu_status, name='cpu_status'),
    path('detail/<int:pk>/', views.detail_log, name='detail_log'),
]