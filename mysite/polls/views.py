from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.

#def index(request):
    #latest_question_list= Question.objects.order_by('-pub_date') [:5]
    #template= loader.get_template('polls/index.html')
    #context= {
    #    'latest_question_list' : latest_question_list
    #}
    #return HttpResponse(template.render(context, request))

#use shortcuts: render()
def index(request):
    latest_question_list= Question.objects.order_by('-pub_date') [:5]
    context= {
       'latest_question_list' : latest_question_list
    }
    return render(request, 'polls/index.html', context)

    #----------------------------------
    #output= ','.join([q.question_text for q in latest_question_list])
    #return HttpResponse(output)
    
#/id/
#def detail(request, question_id):
 #   response= "You're looking at question %s" 
  #  return HttpResponse(response %question_id)

#raising 404 error
#def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return render(request, 'polls/detail.html', {'question': question})

#use shortcut: get object 404()
def detail(request, question_id):
    question= get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/detail.html', {'question': question})
    
#def results(request, question_id):
#    response= "You're looking result of question %s"
#    return HttpResponse(response %question_id)

#use function
def results(request, question_id):
    question= get_object_or_404(Question, pk= question_id)
    return render(request, 'polls/results.html', {'question': question})

#def vote(request, question_id):
 #   return HttpResponse("You're voting on question %s"  %question_id)
 
#use http
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) #request.post return ID as string 
    except(KeyError, Choice.DoesNotExist): #request-choice raise key-error without choose, this code check key-error and keep stable questions with error notice
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    

class IndexView(generic.ListView):
    template_name= 'polls/index.html'
    context_object_name= 'latest_question_list'
    def get_queryset(self):
        #return Question.objects.order_by('-pub_date') [:5] #Return the last five published questions.
        return Question.objects.filter(
            pub_date__lte= timezone.now()
        ) .order_by('-pub_date') [:5]
        
        
class DetailView(generic.DetailView):
    model= Question
    template_name= 'polls/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte= timezone.now())   
    
class ResultsView(generic.DetailView):
    model= Question
    template_name= 'polls/results.html'
