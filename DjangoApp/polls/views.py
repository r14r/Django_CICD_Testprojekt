# -*- coding: utf-8 -*-
"""
This module demonstrates... 

Example:
        $ python example_google.py

Section breaks are created by resuming unindented text. Section breaks
are also implicitly created anytime a new section starts.

Attributes:

Todo:
    * For module TODOs
    * You have to also use ``sphinx.ext.todo`` extension

"""

import logging

from django.http import HttpResponseRedirect  # HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Choice, Question

LOGGER = logging.getLogger(__name__)


class IndexView(generic.ListView):
    """
    IndexView:
    """

    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )[:5]


class DetailView(generic.DetailView):
    """DetailView"""

    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    """
    ResultsView:
    """

    model = Question
    template_name = "polls/results.html"


def index(request):
    """ """
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}

    return render(request, "polls/index.html", context)


def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    """
    results:
    """

    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    """
    vote:
    """

    question = get_object_or_404(Question, pk=question_id)

    LOGGER.debug("vote | question = " + str(question))

    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        LOGGER.debug("vote | selected_choice = " + str(selected_choice))

    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice. ID was %d" % question_id,
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
