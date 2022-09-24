from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/create', views.CreatePost.as_view(), name='create_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('about.html', views.about, name="about"),
]