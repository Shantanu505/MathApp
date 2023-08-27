from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path(
        "history", views.get_history, name="history"
    ),
    path("<path:operation>/", views.calculate, name="calculate"),
]
