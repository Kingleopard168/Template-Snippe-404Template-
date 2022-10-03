from textwrap import indent
from django.urls import path

from challenges import views

from . import views
urlpatterns = [
    path("", views.index, name="index"), #/challenges/
    path("<int:month>",views.monthly_challenge_by_number),
    path("<str:month>",views.monthly_challenge, name="monthly_challenges")
]