from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm, SnippetForm

# Create your views here.
def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():

            project_name = form.cleaned_data['project_name']
            client = form.cleaned_data['client']
            email = form.cleaned_data['email']
            num_sample = form.cleaned_data['num_sample']
            description = form.cleaned_data['description']
            sample_type = form.cleaned_data['sample_type']
            extraction_method = form.cleaned_data['extraction_method']
            sample_cleanup = form.cleaned_data['sample_cleanup']
            analysis_instrumentation = form.cleaned_data['analysis_instrumentation']



            print(f'project name:{project_name}, client:{client}, email:{email}, number of samples:{num_sample}, description:{description}, sample type:{sample_type}, extraction method:{extraction_method}, sample cleanup: {sample_cleanup}, analysis instrumentation: {analysis_instrumentation}')
            

    form = ContactForm()
    return render(request, 'form.html',{'form': form})

def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()


            

    form = SnippetForm()
    return render(request, 'form.html',{'form': form})
