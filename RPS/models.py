from django.contrib.auth.models import User
from django.db import models


class Choice(models.Model):
    rps = models.CharField(max_length=255)

    def __str__(self):
        return self.rps


class Result(models.Model):
    attacker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='def_result')
    defender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='atk_result')
    atk_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='def_choice')
    def_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, related_name='atk_choice', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    atk_status = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.attacker}vs{self.defender}'
