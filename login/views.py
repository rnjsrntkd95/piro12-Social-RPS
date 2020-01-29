from django.shortcuts import render


def social_login(request):
    return render(request, 'login/social_login.html')