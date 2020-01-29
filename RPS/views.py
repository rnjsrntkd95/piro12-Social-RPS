import random
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from RPS.games import game
from RPS.models import Result, Choice


def home(request):
    return render(request, 'home.html')


def log(request, pk):
    result = Result.objects.filter(Q(attacker=pk) | Q(defender=pk)).order_by('created_at')
    context = {
        'result': result
    }
    return render(request, 'RPS/log.html', context)


def attack(request, pk):
    if request.method == 'POST':
        attacker = User.objects.get(username=request.POST['attacker'])
        defender = User.objects.get(username=request.POST['defender'])
        atk_choice = Choice.objects.get(rps=request.POST['atk_choice'])

        Result.objects.create(attacker=attacker, defender=defender, atk_choice=atk_choice)

        return redirect('RPS:log', pk)
    else:
        attacker = User.objects.get(pk=pk)
        defender = User.objects.exclude(pk=pk)
        choice = Choice.objects.all()

        context = {
            'attacker': attacker,
            'defender': defender,
            'choice': choice
        }

        return render(request, 'RPS/attack.html', context)


def defense(request, log_pk, pk):
    if request.method == 'POST':
        result = Result.objects.get(pk=log_pk)

        atk_choice = result.atk_choice
        def_choice = Choice.objects.get(rps=request.POST['def_choice'])
        result.atk_status = game(atk_choice.rps, def_choice.rps)
        result.save()
        a = Result.objects.get(pk=log_pk)
        print(a.atk_status)

        return redirect(reverse('RPS:log', kwargs={'pk': pk}))
    else:
        result = Result.objects.get(pk=log_pk)

        attacker = result.attacker
        defender = result.defender
        choice = Choice.objects.all()

        context = {
            'attacker': attacker,
            'defender': defender,
            'choice': choice
        }

        return render(request, 'RPS/defense.html', context)


def offline_log(request):
    logs = []
    game = {}
    with open('log.txt', 'r', encoding='utf-8') as file:
        for row in file.readlines():
            set = row.split()
            game['human'] = set[0]
            game['computer'] = set[1]
            game['status'] = set[2]
            logs.append(game)
    context = {
        'logs': logs
    }
    return render(request, 'RPS/offline_log.html', context)


def offline_play(request):
    if request.method == 'POST':
        rps = ['가위', '보', '바위']
        req = request.POST
        computer = random.choice(rps)
        status = game(req['human'], computer)
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f"{req['human']} {computer} {status}\n")

            return redirect('RPS:offline_log')
    else:
        return render(request, 'RPS/offline_play.html')
