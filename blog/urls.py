from django.urls import path
from .views import post_list , post_detail , new_post , about_html

urlpatterns = [
    path('', post_list),
    path('<int:id>' , post_detail),
    path('new' , new_post),
    path('' , about_html)
]