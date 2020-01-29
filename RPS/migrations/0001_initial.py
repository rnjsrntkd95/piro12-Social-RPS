# Generated by Django 2.2.9 on 2020-01-29 04:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atk_choice', models.CharField(max_length=255)),
                ('def_choice', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('atk_status', models.CharField(max_length=255)),
                ('attacker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='def_result', to=settings.AUTH_USER_MODEL)),
                ('defender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='atk_result', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atk_choice', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('attacker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='def_player', to=settings.AUTH_USER_MODEL)),
                ('defender', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='atk_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]