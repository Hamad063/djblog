from blog.models import blog
from about.models import about
from django.urls import path
from .views import post_list , post_detail , new_post , edit_post , delete_post , about_html , test_html 

app_name='blog'


urlpatterns = [
    path('', post_list , name= 'post_list'),
    path('<int:id>' , post_detail , name= 'post_detail'),
    path('<int:id>/edit' , edit_post , name='edit_post'),
    path('<int:id>/delete' , delete_post , name='delete_post'),
    path('new' , new_post , name= 'new_post'),
    path('' , about_html , name= 'about_html'),
    path('' , test_html , name= 'test_html'),
]