from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import DiscoveryForm
from .models import Element

# Home View
def home(request):
    return render(request, 'home.html')

# About View
def about(request):
    return render(request, 'about.html')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discoveries'] = self.object.discovery_set.all()
        context['discovery_form'] = DiscoveryForm()  # Add the form to the context
        return context

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['discoveries'] = self.object.discovery_set.all()  # Add related discoveries
        return context

def elements(request):
    return render(request, 'elements/index.html')

def periodic_table(request):
    elements = Element.objects.all()
    return render(request, 'periodic_table.html', {'elements': elements})

def element_detail(request, element_id):
    element = Element.objects.get(id=element_id)
    return render(request, 'elements/detail.html', {'element': element})
# main-app/views.py

class ElementCreate(CreateView):
    model = Element
    fields = ['name', 'symbol', 'atomic_number', 'atomic_weight', 'description', 'group', 'period']
class ElementUpdate(UpdateView):
    model = Element
    fields = ['symbol', 'atomic_number', 'atomic_weight', 'description', 'group', 'period']

class ElementDelete(DeleteView):
    model = Element
    success_url = reverse_lazy('element_list')


# class Element:
#     def __init__(self, name, symbol, atomic_number, atomic_weight, description, group, period):
#         self.name = name
#         self.symbol = symbol
#         self.atomic_number = atomic_number
#         self.atomic_weight = atomic_weight
#         self.description = description
#         self.group = group
#         self.period = period


# elements = [
#     Element('Hydrogen', 'H', 1, 1.008, 'The lightest element. Colorless, odorless gas.', 1, 1),
#     Element('Helium', 'He', 2, 4.0026, 'An inert noble gas, used in balloons.', 18, 1),
#     Element('Lithium', 'Li', 3, 6.94, 'A soft, silvery-white alkali metal.', 1, 2),
#     Element('Carbon', 'C', 6, 12.011, 'Essential for life. Found in organic compounds.', 14, 2),
#     Element('Oxygen', 'O', 8, 15.999, 'Vital for respiration, highly reactive.', 16, 2),
#     Element('Gold', 'Au', 79, 196.967, 'A precious metal known for its malleability and color.', 11, 6),
#     Element('Uranium', 'U', 92, 238.02891, 'Radioactive element used in nuclear power.', 3, 7)
# ]