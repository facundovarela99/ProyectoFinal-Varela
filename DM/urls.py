from uuid import UUID
from django.urls import path, re_path
from .views import *


UUID_CANAL_REGEX = r'canal/(?P<pk>[a-f0-9]{8}-?[a-f0-9]{4}-?4[a-f0-9]{3}-?[89ab][a-f0-9]{3}-?[a-f0-9]{12})'
urlpatterns = [

re_path(UUID_CANAL_REGEX, CanalDetailView.as_view()),

path('dm/<str:username>', mensajes_privados, name='mensajes_privados'),
path('ms/<str:username>', DetailMs.as_view(), name='DetailMs'),
path('Inbox', Inbox.as_view(), name='Inbox'),
# path('buscar/<str:username>', buscar, name='buscar'),
]