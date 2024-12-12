from django.shortcuts import render

from django.http import HttpResponse

class Element:
    def __init__(self, name, symbol, atomic_number, atomic_weight, description, group, period):
        self.name = name
        self.symbol = symbol
        self.atomic_number = atomic_number
        self.atomic_weight = atomic_weight
        self.description = description
        self.group = group
        self.period = period


elements = [
    Element('Hydrogen', 'H', 1, 1.008, 'The lightest element. Colorless, odorless gas.', 1, 1),
    Element('Helium', 'He', 2, 4.0026, 'An inert noble gas, used in balloons.', 18, 1),
    Element('Lithium', 'Li', 3, 6.94, 'A soft, silvery-white alkali metal.', 1, 2),
    Element('Carbon', 'C', 6, 12.011, 'Essential for life. Found in organic compounds.', 14, 2),
    Element('Oxygen', 'O', 8, 15.999, 'Vital for respiration, highly reactive.', 16, 2),
    Element('Gold', 'Au', 79, 196.967, 'A precious metal known for its malleability and color.', 11, 6),
    Element('Uranium', 'U', 92, 238.02891, 'Radioactive element used in nuclear power.', 3, 7)
]

def home(request):
    return HttpResponse('<h1>Welcome to the Interactive Periodic Table</h1><p>Explore the elements!</p>')

def about(request):
    return render(request, 'about.html')

def elements(request):
    return render(request, 'elements.html')


