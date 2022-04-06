from django.urls import path,include
from .views import MusicListView

urlpatterns = [
    path('songs', MusicListView.as_view(), name = 'songs')
]
