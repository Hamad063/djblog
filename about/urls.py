from .views import about1
from django.urls import path


urlpatterns = [
    path('', about1),
]