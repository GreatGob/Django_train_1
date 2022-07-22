from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from .models import Companies, Employees
# Create your views here.
def index(request):
    companies_list= Companies.objects.order_by('-pub_date') [:5]
    context= {
        'companies_list':companies_list
    }
    return render(request, 'companies/index.html', context)

def detail(request, question_id):
    companies= get_object_or_404(Companies, pk= question_id)
    return render(request, 'companies/detail.html', {'company': companies})
