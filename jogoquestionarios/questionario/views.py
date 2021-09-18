from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from .models import Question
from django.utils import timezone

def index(request):
	return HttpResponse("Olá mundo")
