from django.shortcuts import render, redirect
from .models import Add
from .forms import AddForm

# Create your views here.
def index(request):
    diary = Add.objects.order_by('-date_added')
    content = {'diary' : diary}
    return render(request, 'entries/index.html', content)

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddForm()
    content = {'form': form}
    return render(request, 'entries/add.html', content)
