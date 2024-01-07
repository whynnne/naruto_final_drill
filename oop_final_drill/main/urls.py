# naruto_shippuden/urls.py
from django.urls import path
from .views import HomeView, VillageListView,  CharacterListView,  JutsuListView, CharacterCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('villages/', VillageListView.as_view(), name='village_list'),
    path('characters/', CharacterListView.as_view(), name='character_list'),
    path('jutsus/', JutsuListView.as_view(), name='jutsu_list'),
    path('character/create/', CharacterCreateView.as_view(), name='create_character'),
]
