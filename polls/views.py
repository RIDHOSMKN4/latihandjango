from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from .models import Question

def index(request: HttpRequest):
    lates_question_list = Question.objets.order_by("-pub_date")[:5]
    output = ", ".join([q.Question_text for q in lates_question_list])
    return HttpResponse(output)

def detail(request: HttpRequest, question_id: int):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request: HttpRequest, question_id: int):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request: HttpRequest, question_id: int):
    return HttpResponse("You're voting on question %s." % question_id)