import copy
import random
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from RPS.games import game
from RPS.models import Result, Choice


def main(request):
    return render(request, 'RPS/main.html')


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
        return render(request, 'RPS/fight.html', context)


def defense(request, log_pk, pk):
    if request.method == 'POST':
        result = Result.objects.get(pk=log_pk)

        atk_choice = result.atk_choice
        def_choice = Choice.objects.get(rps=request.POST['def_choice'])
        result.atk_status = game(atk_choice.rps, def_choice.rps)
        result.def_choice = def_choice
        result.save()
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

        return render(request, 'RPS/react.html', context)


def offline_log(request):
    logs = []
    with open('log.txt', 'r', encoding='utf-8') as file:
        for row in file.readlines():
            game = {}
            human, computer, status = row.split()
            game['human'] = human
            game['computer'] = computer
            game['status'] = status
            logs.append(game)
    context = {
        'logs': logs
    }
    return render(request, 'RPS/human.html', context)


def offline_play(request):
    rps = ['가위', '보', '바위']
    if request.method == 'POST':
        req = request.POST
        computer = random.choice(rps)
        status = game(req['human'], computer)
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f"{req['human']} {computer} {status}\n")

            return redirect('RPS:offline_log')
    else:
        context = {
            'rps': rps
        }
        return render(request, 'RPS/cpu_fight.html', context)


def cpu_status(request, pk):
    count = 0
    game = {}
    with open('log.txt', 'r', encoding='utf-8') as file:
        for row in file.readlines():

            count += 1
            if count != pk:
                continue
            human, computer, status = row.split()
            game['human'] = human
            game['computer'] = computer
            game['status'] = status
            break
    print(game)
    context = {
        'game': game
    }
    return render(request, 'RPS/cpu_status.html', context)


def detail_log(request, pk):
    result = Result.objects.get(pk=pk)
    context= {
        'result': result
    }
    return render(request, 'RPS/detail_log.html', context)

