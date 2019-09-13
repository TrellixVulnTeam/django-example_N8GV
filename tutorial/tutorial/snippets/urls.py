from django.urls import path,re_path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    # match the url pattern and the class name ow views.py
    path('snippets/', views.SnippetList.as_view()),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    path('snippets/last', views.SnippetLast.as_view()),
    re_path(r'^snippets/(?P<rFrom>[0-9]+)-(?P<rTo>[0-9]+)/$', views.SnippetRange.as_view()),
    # mixins
    path('snippets/m', views.SnippetListMixins.as_view()),
    re_path(r'^snippets/m(?P<pk>[0-9]+)/$', views.SnippetDetailMixins.as_view()),
    #generic
    path('snippets/g', views.SnippetListGeneric.as_view()),
    re_path(r'^snippets/g(?P<pk>[0-9]+)/$', views.SnippetDetailGeneric.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)