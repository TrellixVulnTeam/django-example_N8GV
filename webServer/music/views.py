from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Album
from django.views import generic
from django.shortcuts import render,redirect
from .models import Album
from .form import UserForm

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_title','gerne','album_logo']
    
class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_title','gerne','album_logo']

class AlbumDelete(DeleteView):
    model = Album
    fields = ['artist','album_title','gerne','album_logo']
    success_url = reverse_lazy('music:index')