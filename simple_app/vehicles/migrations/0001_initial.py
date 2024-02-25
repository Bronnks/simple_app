# Generated by Django 3.2.24 on 2024-02-25 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tank_name', models.CharField(max_length=50)),
                ('tank_type', models.CharField(max_length=20)),
                ('tank_description', models.TextField(max_length=100)),
                ('damage_points', models.IntegerField()),
                ('armor_points', models.IntegerField()),
                ('speed', models.IntegerField()),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
