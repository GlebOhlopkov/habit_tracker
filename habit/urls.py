from django.urls import path

from habit.views import HabitCreateAPIView, HabitListAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, \
    HabitDestroyAPIView

app_name = 'habit'

urlpatterns = [
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('list/', HabitListAPIView.as_view(), name='habit_list'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
