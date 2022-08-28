from django.urls import path
from .views import CounterView

urlpatterns = [
    path("views-counter/", CounterView.as_view()),
]
