# Generated by Django 3.2.24 on 2024-02-25 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_playervehicles'),
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerRanking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking_points', models.IntegerField()),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.players')),
            ],
        ),
    ]
