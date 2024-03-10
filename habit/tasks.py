from celery import shared_task

from habit.models import Habit
from habit.services import send_tg_bot_massage


@shared_task
def check_habit_by_hour():
    habits = Habit.objects.filter(period='HOUR').all()
    for habit in habits:
        send_tg_bot_massage(habit)


@shared_task
def check_habit_by_day():
    habits = Habit.objects.filter(period='DAY').all()
    for habit in habits:
        send_tg_bot_massage(habit)


@shared_task
def check_habit_by_week():
    habits = Habit.objects.filter(period='WEEK').all()
    for habit in habits:
        send_tg_bot_massage(habit)
