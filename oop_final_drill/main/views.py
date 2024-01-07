from django.views.generic import ListView, TemplateView, CreateView
from .models import Village, Character, Jutsu
from .forms import CharacterForm
from django.urls import reverse_lazy
class HomeView(TemplateView):
    template_name = 'home.html'
class VillageListView(ListView):
    model = Village
    template_name = 'village_list.html'
    context_object_name = 'villages'


class CharacterListView(ListView):
    model = Character
    template_name = 'character_list.html'
    context_object_name = 'characters'



class JutsuListView(ListView):
    model = Jutsu
    template_name = 'jutsu_list.html'
    context_object_name = 'jutsus'
    paginate_by = 0
    

from .forms import CharacterForm

class CharacterCreateView(CreateView):
    model = Character
    form_class = CharacterForm
    template_name = 'naruto_shippuden/character_form.html'
    success_url = reverse_lazy('character_list')  # Replace 'character_list' with the URL name of your character list view