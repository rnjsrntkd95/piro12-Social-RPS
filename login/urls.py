from django.urls import path, include
from login.views import social_login, general_login, sign_up, logout

# app_name = 'login'

urlpatterns = [
    path('', social_login, name='social_login'),
    path('general/', general_login, name='general_login'),
    path('signup/', sign_up, name='sign_up'),
    path('logout/', logout, name='logout'),
    path('accounts/', include('allauth.urls')),
]