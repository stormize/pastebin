from django.urls import path
from .views import Events,get_private,get_public
app_name = 'pastebins'
urlpatterns = [
    path('',Events.as_view(),name="api"),
    path('public',get_public.as_view(),name="api"),
    path('private',get_private.as_view(),name="api"),
]