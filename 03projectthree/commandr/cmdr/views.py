from django.views.generic import ListView

from .models import Cmdr

class HomePageView(ListView):
    model = Cmdr
    template_name = 'home.html'
