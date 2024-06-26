from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.blog_list, name='all'),
    path('create/',views.blog_create, name='create'),
    path('<slug>',views.blog_detail, name='details'),
]