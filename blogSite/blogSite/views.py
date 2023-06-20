from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect


def home(request):
    return render(request,"index.html")


from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})