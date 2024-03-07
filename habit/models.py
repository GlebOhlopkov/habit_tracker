from datetime import timedelta

from django.db import models

from users.models import User


class Habit(models.Model):
    PERIOD_OF_HABIT = [
        ('HOUR', 'one time in hour'),
        ('DAY', 'one time in day'),
        ('WEEK', 'one time in week'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='owner')
    place = models.CharField(max_length=200, verbose_name='place')
    time = models.TimeField(verbose_name='time')
    action = models.CharField(max_length=200, verbose_name='action')
    is_nice_habit = models.BooleanField(null=True, blank=True, verbose_name='is_nice_habit')
    nice_habit = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='nice_habit')
    period = models.CharField(max_length=20, choices=PERIOD_OF_HABIT, default='DAY', verbose_name='period')
    reward = models.CharField(max_length=200, verbose_name='reward')
    duration = models.DurationField(default=timedelta(minutes=2), verbose_name='duration')
    is_public = models.BooleanField(default=False, verbose_name='is_public')

    def __str__(self):
        return f'{self.owner} - {self.action}'

    class Meta:
        verbose_name = 'habit'
        verbose_name_plural = 'habits'
