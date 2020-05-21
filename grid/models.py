from django.db.models import Model, IntegerField, CharField

# Create your models here.
class Grid(Model):
  x = IntegerField()
  y = IntegerField()
  word = CharField(max_length=32)
