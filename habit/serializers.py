from rest_framework import serializers

from habit.models import Habit
from habit.validators import validator_habit_fields


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [validator_habit_fields]
