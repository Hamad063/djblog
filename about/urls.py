from blog.views import about_html
from about.models import about
from django.urls import path


urlpatterns = [
    path('', about_html),
]