from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Todo
from django.views.generic.list import ListView



class TodoListView(ListView):
    model = Todo

    def get_context_date(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        return context

def top(request):
  items = Todo.objects.all().order_by('-updated_datetime')
  return render(request, 'app/top.html', { 'items': items })


