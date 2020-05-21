from django.shortcuts import render
from .models import Grid
from django.views.decorators.csrf import csrf_exempt

def home(request):
  return render(request, 'index.html')

@csrf_exempt
def grid(request, x, y):
  try:
    grid = Grid.objects.get(x=x, y=y)
    word = grid.word
  except Grid.DoesNotExist:
    grid = None
    word = None
  
  if word and word.strip() == '':
    word = None
  
  if (not word or word.strip()=='') and request.method == "POST":
    word = request.POST.get('word')
    if grid:
      grid.word = word
      grid.save()
    else:
      Grid(x=x, y=y, word=word).save()


  return render(request, 'grid.html', dict(x=int(x)*130, y=int(y)*25, word=word))
