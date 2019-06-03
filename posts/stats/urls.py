from django.urls import path
from .views import pd_stats
urlpatterns = [
    path('',pd_stats),
]