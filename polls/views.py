# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from models import Poll, Choice
from fiber.views import FiberPageMixin


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published polls."""
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes any polls not yet published."""
        return Poll.objects.filter(pub_date__lte=timezone.now())


#class ResultsView(generic.DetailView):
#    model = Poll
#    template_name = 'polls/results.html'


class ResultsView(FiberPageMixin, generic.DetailView):
    """
    Using django Class Based Detail View
    """
    model = Poll  # model that model view is associated with
    template_name = 'polls/results_fiber.html'  # template

    def get_fiber_page_url(self):  # mixin with django fiber
        # The mixin needs to know the url for the associate django page
        # we get this using the reverse lookup to find the appropriate page object
        # from the django page tree. This example is complicated by the fact that the
        # url requires a variable, the poll object id. The value of the current poll object
        # is accessible in the Detail View instance. Every detail view is associated with
        # an object.
        #return reverse('polls:results', args=[self.object.id])
        return 'polls'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
          'poll' : p,
          'error_message' : "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

