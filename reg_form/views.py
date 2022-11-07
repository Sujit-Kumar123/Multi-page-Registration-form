from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import FormoneForm, EducationForm, UploadingDocumentForm
from django.contrib import messages

# Create your views here.
# First form
def form_one(request):
    if request.method=='POST':
        refm=FormoneForm(request.POST)
        if refm.is_valid():
            refm.save()
            return HttpResponseRedirect('/edu/')

    else:
        refm=FormoneForm()
    return render(request,'reg_form/formone.html',{'form':refm})


# Second Form
def form_two(request):
    if request.method=='POST':
        refm=EducationForm(request.POST)
        if refm.is_valid():
            refm.save()
            return HttpResponseRedirect('/upload/')
    else:
        refm=EducationForm()
    return render(request,'reg_form/formtwo.html',{'form':refm})


def form_three(request):
    if request.method=='POST':
        resumfm=UploadingDocumentForm(request.POST,files=request.FILES)
        if resumfm.is_valid():
            resumfm.save()
            return HttpResponseRedirect('/')
    else:
        resumfm=UploadingDocumentForm()
    return render(request,'reg_form/formthree.html',{'form':resumfm})