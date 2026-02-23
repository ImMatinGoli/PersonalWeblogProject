from django.urls import path
from .views import *

urlpatterns = [
    path('', posts_list_view, name='posts_list'),
    path('create/', post_create_view, name='post_create'),
    path('<int:pk>/', posts_detail_view, name='post_detail'),
    path('<int:pk>/update/', post_update_view, name='post_update'),
    path('<int:pk>/update/access_denied', access_denied_update_view, name='post_update_access_denied'),
    path('<int:pk>/delete/', post_delete_view, name='post_delete'),
    path('category/<str:name>/', category_posts_view, name='category_posts'),
    path('like/<int:pk>/', like_post_view, name='like_post'),
    path('search/', search_view, name='search'),
    path('search/live/', live_search_view, name='live_search'),
]
