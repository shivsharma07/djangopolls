#from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http.response import Http404

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    #return HttpResponse("Hello, world! You're at the polls index.")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = RequestContext(request, {
#         'latest_question_list': latest_question_list,
#     })
#     return HttpResponse(template.render(context))
    context = {'latest_question_list' : latest_question_list}
    return render(request, 'polls/index.html', context)
#     output = ', '.join([p.question_text for p in latest_question_list])
#     return HttpResponse(output)
    
def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

@login_required
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)