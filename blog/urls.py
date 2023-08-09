
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:post_id>/', views.post, name='post'),
]
