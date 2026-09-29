from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Project

def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()

    projects = Project.objects.all().order_by('-created_at')

    return render(request, 'index.html', {
        'form': form,
        'projects': projects
    })