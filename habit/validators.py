from datetime import timedelta

from rest_framework import serializers

from habit.models import Habit


class RewardOrNiceHabitValidator:

    def __call__(self, value):
        nice_habit = bool(dict(value).get('nice_habit'))
        reward = bool(dict(value).get('reward'))

        if nice_habit and reward:
            raise serializers.ValidationError(
                'Habit can have only reward or nice habit')


class IsNiceHabitValidator:

    def __call__(self, value):
        nice_habit = dict(value).get('nice_habit')
        if nice_habit:
            habit = Habit.objects.get(pk=nice_habit.id)
            if not habit.is_nice_habit:
                raise serializers.ValidationError(
                    'Habit can connected only with nice habit')


class IsNiceHabitHaveRewardValidator:

    def __call__(self, value):
        is_nice_habit = dict(value).get('is_nice_habit')
        reward = bool(dict(value).get('reward'))
        nice_habit = bool(dict(value).get('nice_habit'))

        if is_nice_habit and reward or is_nice_habit and nice_habit:
            raise serializers.ValidationError(
                'Nice habit cant have reward or another nice habit')

# def validator_habit_fields(value):
#     try:
#         if value['is_nice_habit']:
#             if value['nice_habit'] or value['reward']:
#                 raise serializers.ValidationError(
#                     'Nice habit cant have reward or another nice habit')
#     except KeyError:
#         pass
#     try:
#         if value['nice_habit'] and value['reward']:
#             raise serializers.ValidationError(
#                 'Habit can have only reward or nice habit')
#     except KeyError:
#         pass
#     try:
#         if value['nice_habit']:
#             if not value['nice_habit'].is_nice_habit:
#                 raise serializers.ValidationError(
#                     'Habit can connected only with nice habit')
#     except KeyError:
#         pass
#     try:
#         if value['duration'] > timedelta(minutes=2):
#             raise serializers.ValidationError(
#                 'Habits action duration must be less than 2 min (120 sec)')
#     except KeyError:
#         pass
