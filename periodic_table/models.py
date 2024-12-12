from django.db import models

class Element(models.Model):
    name = models.CharField(max_length=100)  # Full name of the element (e.g., "Hydrogen")
    symbol = models.CharField(max_length=3, unique=True)  # Chemical symbol (e.g., "H")
    atomic_number = models.PositiveIntegerField(unique=True)  # Atomic number (e.g., 1 for Hydrogen)
    atomic_weight = models.FloatField()  # Atomic weight (e.g., 1.008 for Hydrogen)
    description = models.TextField(max_length=500)  # Brief description or fact about the element
    group = models.PositiveIntegerField()  # Group number on the periodic table
    period = models.PositiveIntegerField()  # Period number on the periodic table

    def __str__(self):
        return f"{self.name} ({self.symbol})"

