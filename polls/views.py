from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from polls.models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('polls/index.html')
    context = {
            'latest_question_list': latest_question_list,
            }
    return render(request, 'polls/index.html', context)
#    return HttpResponse(template.render(context, request))
#    output = ', '.join([q.question_text for q in latest_question_list])
#    return HttpResponse(output)
#    return HttpResponse("Hello, world!  This is the 'polls' index view.")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist!")
    return render(request, 'polls/detail.html', 
            {'question': question})
#    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html',
            {'question': question})
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a valid choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after
        # successfully handling POST data to prevent data
        # from being posted twice if user presses "Back" button.
        return HttpResponseRedirect(reverse('polls:results',
            args=(question.id,)))
#    return HttpResponse("You're voting on question %s." % question_id)

