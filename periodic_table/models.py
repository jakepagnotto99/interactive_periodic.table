from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
    
DISCOVERY_TYPES = (
    ('S', 'Synthesized'),
    ('N', 'Naturally Found'),
    ('D', 'Discovered'),
)

class Element(models.Model):
    name = models.CharField(max_length=100)  # Full name of the element (e.g., "Hydrogen")
    symbol = models.CharField(max_length=3, unique=True)  # Chemical symbol (e.g., "H")
    atomic_number = models.PositiveIntegerField(unique=True)  # Atomic number (e.g., 1 for Hydrogen)
    atomic_weight = models.FloatField()  # Atomic weight (e.g., 1.008 for Hydrogen)
    description = models.TextField(max_length=500)  # Brief description or fact about the element
    group = models.PositiveIntegerField()  # Group number on the periodic table
    period = models.PositiveIntegerField()  # Period number on the periodic table
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this cat's details
        return reverse('element_detail', kwargs={'element_id': self.id})

class Discovery(models.Model):
    date = models.DateField('Discovery Date')
    type = models.CharField(
        max_length=1,
        choices=DISCOVERY_TYPES,
        default=DISCOVERY_TYPES[0][0],
    )
    discoverer = models.CharField('Discoverer', max_length=100)
    # Link each discovery to a specific element
    element = models.ForeignKey('Element', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_type_display()} on {self.date} by {self.discoverer}"

    class Meta:
        ordering = ['-date']  # Show the most recent discoveries first

class QuizQuestion(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)  # A, B, C, D

    def __str__(self):
        return f"Question: {self.question[:50]}..."

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - Score: {self.score}"
 
