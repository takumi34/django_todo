from django.shortcuts import render
from django.shortcuts import get_object_or_404

def top(request):
  return render(request, 'app/top.html')


