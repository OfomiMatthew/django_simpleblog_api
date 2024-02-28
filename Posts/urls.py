from django.urls import path
from . import views 

urlpatterns = [
    path('',views.homePage,name="home"),
    path('posts',views.list_posts,name="posts"),
    path('post/<int:index>',views.post_detail,name='post')
]
