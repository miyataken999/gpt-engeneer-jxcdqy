from django.shortcuts import render, redirect
from .forms import JewelryForm
from .models import Jewelry

def index(request):
    return render(request, 'index.html')

def evaluate(request):
    if request.method == 'POST':
        form = JewelryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('evaluate')
    else:
        form = JewelryForm()
    return render(request, 'evaluate.html', {'form': form})

def estimate_value(request):
    # TO DO: implement estimate value logic
    pass