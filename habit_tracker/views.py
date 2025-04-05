from rest_framework import generics

from habit_tracker.models import Habit
from habit_tracker.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """Эндпоинт создания привычки"""

    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    """Эндпоинт списка привычек"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Эндпоинт просмотра привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт изменения привычки"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт удаления привычки"""

    queryset = Habit.objects.all()
