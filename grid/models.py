from django.db.models import *

# Create your models here.
class Grid(Model):
  x = IntegerField()
  y = IntegerField()
  word = CharField(max_length=32)
