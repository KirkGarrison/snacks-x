from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Snack


class SnackListView(ListView):
    template_name = 'snacks/snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snacks/snack_detail.html'
    model = Snack

class SnackCreateView(CreateView):
    template_name = 'snacks/snack_create.html'
    model = Snack
    fields = ['name', 'description', 'purchaser']

class SnackDeleteView(DeleteView):
    template_name = 'snacks/snack_delete.html'
    model = Snack
    success_url = reverse_lazy('snack_list')

class SnackUpdateView(UpdateView):
    template_name = 'snacks/snack_update.html'
    model = Snack
    fields = ['name', 'description']
    
