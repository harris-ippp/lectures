from django.db import models 

# Create your models here.
STATES = ( ('AK', 'Alaska'), ('AL', 'Alabama'), # ...
           ('WV', 'West Virginia'), ('WY', 'Wyoming'))

class Input(models.Model): # our model inherits from Django.
  state = models.CharField(max_length=2, choices=STATES)
  name  = models.CharField(max_length=50)
