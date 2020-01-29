from django.contrib.auth.models import User
from django.db import models


class Player(models.Model):
    attacker = models.OneToOneField(User, on_delete=models.CASCADE, related_name='def_player')
    atk_choice = models.CharField(max_length=255)
    defender = models.OneToOneField(User, on_delete=models.CASCADE, related_name='atk_player')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.attacker


class Result(models.Model):
    attacker = models.OneToOneField(User, on_delete=models.CASCADE, related_name='def_result')
    defender = models.OneToOneField(User, on_delete=models.CASCADE, related_name='atk_result')
    atk_choice = models.CharField(max_length=255)
    def_choice = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    atk_status = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.attacker}vs{self.defender}'
