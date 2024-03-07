from django.shortcuts import render
from rest_framework import generics

from habit.models import Habit
from habit.paginators import HabitPagePagination
from habit.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    # permission_classes =

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes =
    pagination_class = HabitPagePagination

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes =
    pagination_class = HabitPagePagination

    def get_queryset(self):
        return super().get_queryset().filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes =


class HabitUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    # permission_classes =


class HabitDestroyAPIView(generics.DestroyAPIView):
    queryset = Habit.objects.all()
    # permission_classes =
