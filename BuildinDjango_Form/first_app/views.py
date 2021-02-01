from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from first_app import views
from first_app import forms
# Create your views here.
def index(request):
    diction={}


    if request.method=="POST":
        form_obj=forms.UserForm(request.POST)
        diction.update({"form_obj":form_obj})
        if form_obj.is_valid():
            diction.update({"email":form_obj.cleaned_data["email"]})
            diction.update({"vmail":form_obj.cleaned_data["vmail"]})
            diction.update({"title":"Yes"})
    else:
        form_obj=forms.UserForm()
        diction.update({ "form_obj":form_obj })
    return render(request,'first_app/index.html',context=diction)
