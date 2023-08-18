from django.urls import path
from .views import *

urlpatterns = [
    path('home-img-get/', home_img_get),
    path('advice-get/', advice_get),
    path('player-get/', player_get),
    path('blog-get/', blog_get),
    path('table-get/', table_get),
    path('sponsor-get/', sponsor_get),
    path('bobur-arena-get/', boburArena_get),
    path('rahbariyat-get/', rahbariyat_get),
    path('club-get/', club_get),
]
