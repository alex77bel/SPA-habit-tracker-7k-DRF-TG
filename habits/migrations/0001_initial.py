# Generated by Django 4.2.4 on 2023-08-10 16:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='место выполнения привычки')),
                ('time', models.TimeField(default=django.utils.timezone.now, verbose_name='время выполнения привычки')),
                ('action', models.CharField(max_length=150, verbose_name='действие привычки')),
                ('is_public', models.BooleanField(default=True, verbose_name='признак публичности привычки')),
                ('duration', models.PositiveIntegerField(default=120, verbose_name='длительность выполнения в секундах')),
                ('is_enjoyable_habit', models.BooleanField(default=False, verbose_name='признак приятной привычки')),
                ('fee', models.CharField(blank=True, max_length=150, null=True, verbose_name='вознаграждение')),
                ('periodicity', models.PositiveSmallIntegerField(default=1, verbose_name='периодичность выполнения привычки, раз в сутки')),
                ('enjoyable_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habit', verbose_name='приятная привычка')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('time',),
            },
        ),
    ]
