from django.shortcuts import render
from . import forms

# Create your views here.
def vista(request):
    if request.method=="POST":
        form=forms.Formulario(request.POST, request.FILES)
        if form.is_valid():
            form.save().save()
    else:
        form=forms.Formulario()

    return render(
            request,
            template_name="dothetest/template.html",
            context={'form':form})

