from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.views.generic import ListView, DetailView
from polls.models import Question

from .models import Choice, Question
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
from django.urls.base import reverse_lazy #reverse_lazy를 선언 

from mysite.views import LoginRequiredMixin
from django.views.generic.edit import FormView

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]



class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
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

class PollsCreateView(LoginRequiredMixin, CreateView):
        model = Question
        fields = ['question_text', 'pub_date']
        success_url = reverse_lazy('polls:index')

        def form_vaild(self, form):
            form.instance.owner = self.request.user
            return super(PollsCreateView, self).form_valid(form)

class PollsChangeLV(LoginRequiredMixin, ListView):
        template_name = 'polls/polls_change_list.html'

        def get_queryset(self):
            return Question.objects.filter(question_text  = self.request.user)

class PollsUpdateView(LoginRequiredMixin, UpdateView):
        model = Question
        fields = ['question_text', 'pub_date']
        success_url = reverse_lazy('polls:index')

class PollsDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')
