from django.urls import path

from habit_tracker.apps import HabitTrackerConfig
from habit_tracker.views import (
    HabitCreateAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView, PublishedHabitListAPIView,
)

app_name = HabitTrackerConfig.name

urlpatterns = [
    path("create/", HabitCreateAPIView.as_view(), name="create-habit"),
    path("", HabitListAPIView.as_view(), name="habits-list"),
    path("public/list", PublishedHabitListAPIView.as_view(), name="public-habits"),
    path("<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("<int:pk>/update/", HabitUpdateAPIView.as_view(), name="habit-update"),
    path("<int:pk>/delete/", HabitDestroyAPIView.as_view(), name="habit-delete"),
]
