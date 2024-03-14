from rest_framework import serializers

from habit.models import Habit
from habit.validators import RewardOrNiceHabitValidator, IsNiceHabitValidator, IsNiceHabitHaveRewardValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardOrNiceHabitValidator(),
            IsNiceHabitValidator(),
            IsNiceHabitHaveRewardValidator(),
        ]
