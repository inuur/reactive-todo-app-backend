from django.urls import path

from .views import ListView

app_name = "lists"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('lists/', ListView.as_view()),
]
