from django.urls import path,re_path
from . import views
app_name = 'music'

urlpatterns = [
    # /music/
    re_path(r'^$', views.IndexView.as_view(),name='index'),
    # /music/<id>
    re_path(r'^(?P<pk>[0-9]+)$',views.DetailView.as_view(),name='detail'),
    # /music/<id>/favorite
    #re_path(r'^(?P<album_id>[0-9]+)/favorite$',views.favorite,name='favorite')
    re_path(r'album/add/$',views.AlbumCreate.as_view(),name='album_add'),
    re_path(r'album/(?P<pk>[0-9]+)$',views.AlbumUpdate.as_view(),name='album_update'),
    re_path(r'album/(?P<pk>[0-9]+)/delete$',views.AlbumDelete.as_view(),name='album_delete'),
]