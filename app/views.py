from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Todo
from django.views.generic.list import ListView
from .forms import TodoForm


# list表示
#class TodoListView(ListView):
    #model = Todo

    #def get_context_date(self, **kwargs):
        #context = super(TodoListView, self).get_context_data(**kwargs)
        #return context

def top(request):
  if request.method == 'GET':
    form = TodoForm
    items = Todo.objects.all().order_by('-updated_datetime')
    return render(request, 'app/top.html', { 'items': items, 'form': form})
  else:
    form = TodoForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('app:top')


