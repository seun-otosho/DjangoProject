from django.urls import path

from apps.members.api.views import hello_world

urlpatterns = [
    path('api/', hello_world),
]
