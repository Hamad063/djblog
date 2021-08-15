from .views import itmes1 , product_html , post_delete , post_edit , test_html , delete_post, edit_post
from django.urls import path


app_name='itmes'

urlpatterns = [
    path('', itmes1),
    path('product' , product_html , name='product_html'),
    path('<int:id>' , edit_post , name='edit_post'),
    path('<int:id>' , delete_post , name='delete_post'),
    path('' , post_delete , name='post_delete'),
    path('' , post_edit , name='post_edit'),
    path('' , test_html , name='test_html'),
]