from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('posts/create', views.CreatePost.as_view(), name='create_post'),
    path('posts/edit/<id>', views.EditPost.as_view(), name='edit_post'),
    path('posts/delete/<id>', views.PostDelete.as_view(), name='delete_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('users/<username>', views.UserProfile.as_view(), name='user_profile'),
    path('profile/create', views.CreateProfile.as_view(), name='create_profile'),
    path('profile/edit/<id>', views.EditProfile.as_view(), name='edit_profile'),
    path('about.html', views.about, name="about"),
    path('contact.html', views.contact, name='contact'),
]