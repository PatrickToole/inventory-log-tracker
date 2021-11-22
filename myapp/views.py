from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from myapp.models import Snippet
from .forms import ContactForm, SnippetForm

# Create your views here.
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            project_name = form.cleaned_data['project_name']



            

    form = ContactForm()
    return render(request, 'form.html',{'form': form})

def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(snippet_detail)              #################### redirect

    form = SnippetForm()
    return render(request, 'form.html',{'form': form})


