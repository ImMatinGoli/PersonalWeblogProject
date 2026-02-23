from django.urls import path
from .views import *

urlpatterns = [
    path('', home_page_view, name='home'),
    path('about_me/', about_me_page_view, name='about_me'),
    path('contact_me/', contact_me_page_view, name='contact_me'),
    path('profile/', profile_edit_view, name='my_profile'),
    path('profile/reset-avatar/', reset_avatar_view , name='reset_avatar'),
]
