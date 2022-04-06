from re import M
from django.forms import models
from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import Q
from .models import Music

# Create your views here.
class MusicListView(ListView):
    model = Music
    template_name = 'music/music-list.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        results = Music.objects.filter(Q(title__icontains = query))
        return results