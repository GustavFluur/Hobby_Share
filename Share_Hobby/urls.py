from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/create', views.CreatePost.as_view(), name='create_post'),
    path('posts/edit/<id>', views.EditPost.as_view(), name='edit_post'),
    path('posts/delete/<id>', views.PostDelete.as_view(), name='delete_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    # Add this later======> path('like/<slug:slug>', views.PostDisLike.as_view(), name='post_dislike'),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name='contact'),
]