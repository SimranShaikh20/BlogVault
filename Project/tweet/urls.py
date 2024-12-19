from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweet_list, name='tweet_list'),  # List and search tweets
    path('create/', views.tweet_create, name='tweet_create'),  # Create a new tweet
    path('edit/<int:tweet_id>/', views.tweet_edit, name='tweet_edit'),  # Edit a tweet
    path('delete/<int:tweet_id>/', views.tweet_delete, name='tweet_delete'),  # Delete a tweet
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
    path('logout/', views.logout_view, name='logout'),  # User logout
]
