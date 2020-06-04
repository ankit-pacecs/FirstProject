from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'FirstApp/index.html')

def training_domain(request,domain_id):
    return HttpResponse("you are in the %s:" % domain_id)

def candidate(request,domain_id):
    response="you are the candidate named %s."
    return HttpResponse(response % domain_id)