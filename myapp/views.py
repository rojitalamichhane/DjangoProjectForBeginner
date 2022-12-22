from django.shortcuts import render

from myapp.forms import CompanyForm, IndustryTypeForm
from myapp.models import IndustryType, Company
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic import (
    TemplateView, CreateView, View, UpdateView, ListView, FormView, DeleteView, DetailView)
    

# Create your views here.

def myform(request):
    return render(request, 'myapp/form.html')


class IndustryTypeCreateView(CreateView):
    template_name = 'myapp/industry.html'
    form_class = IndustryTypeForm
    
    def post(self, request, *args, **kwargs):
        form = IndustryTypeForm(request.POST)
        if form.is_valid():
            industry_type = IndustryType.objects.create(
                name=form.cleaned_data["name"],
            )
            return HttpResponseRedirect(
                reverse_lazy('myapp:industry_create'))
        else:
            print(form.errors)
            return render(request, self.template_name, {
                    'alert_form': form,
            'error': '* There seems to be some error. Please try again !!!'})

class CompanyCreateView(CreateView):
    template_name = 'myapp/form.html'
    form_class = CompanyForm
    
    def post(self, request, *args, **kwargs):
        form = CompanyForm(request.POST)
        if form.is_valid():
            industry_type = Company.objects.create(
                company_name=form.cleaned_data['company_name'],
                owner_name=form.cleaned_data['owner_name'],
                address=form.cleaned_data['address'],
                email=form.cleaned_data['email'],
                contact=form.cleaned_data['contact'],
                industry_type=form.cleaned_data['industry_type']
            )
            return HttpResponseRedirect(
                reverse_lazy('myapp:company_create'))
        else:
            print(form.errors)
            return render(request, self.template_name, {
                    'form': form,
            'error': '* There seems to be some error. Please try again !!!'})


class IndustryList(ListView):
 
    # specify the model for list view
    model = IndustryType
    template_name = 'myapp/list1.html'
    queryset=IndustryType.objects.all


class CompanyList(ListView):
 
    # specify the model for list view
    model = Company
    template_name = 'myapp/list2.html'
    queryset=Company.objects.all