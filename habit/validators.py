from datetime import timedelta

from rest_framework import serializers


def validator_habit_fields(value):
    try:
        if value['is_nice_habit']:
            if value['nice_habit'] or value['reward']:
                raise serializers.ValidationError(
                    'Nice habit cant have reward or another nice habit')
    except KeyError:
        pass
    try:
        if value['nice_habit'] and value['reward']:
            raise serializers.ValidationError(
                'Habit can have only reward or nice habit')
    except KeyError:
        pass
    try:
        if value['nice_habit']:
            if not value['nice_habit'].is_nice_habit:
                raise serializers.ValidationError(
                    'Habit can connected only with nice habit')
    except KeyError:
        pass
    try:
        if value['duration'] > timedelta(minutes=2):
            raise serializers.ValidationError(
                'Habits action duration must be less than 2 min (120 sec)')
    except KeyError:
        pass
