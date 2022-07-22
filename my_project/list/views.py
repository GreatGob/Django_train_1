from django.shortcuts import get_object_or_404, render
from .models import Companies, Details, Employees
from django.http import HttpResponseRedirect
from django.urls import reverse
#from rest_framework.decorators import APIView
#from rest_framework.response import Response
# Create your views here.

def index(request):
    companies_list= Companies.objects.all()
    context= {
       'companies_list' : companies_list
    }
    return render(request, 'list/index.html', context)

def details(request, company_id):
    company= get_object_or_404(Companies, pk= company_id)
    return render(request, 'list/details-company.html',{'company':company})

def employees(request, employee_id):
    employee= get_object_or_404(Employees, pk=employee_id)
    return render(request, 'list/result.html',employee)

def choice(request, company_id):
    company= get_object_or_404(Companies, pk= company_id)
    try:
        selected_choice=company.choice_set.get(pk=request.GET['choice'])
    except(KeyError, Employees.DoesNotExist):
        return render(request, 'list/details.html', {'company': company})
    else:
        return HttpResponseRedirect(reverse('list:results', args=(company.id,)))
        

