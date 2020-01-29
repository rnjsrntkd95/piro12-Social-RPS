from django.urls import path, include

from login.views import social_login

urlpatterns = [
    path('social/', social_login, name='social_login'),
    path('accounts/', include('allauth.urls')),
]