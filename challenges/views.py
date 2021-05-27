from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# only accepts numbers
def monthly_challenge_by_number(request, month):
    return HttpResponse(month)

# only accepts strings
def monthly_challenge(request, month):
    challenge_text = None

    if month == 'january':
        challenge_text = "Eat your vegetables!"
    elif month == 'february':
        challenge_text = "Walk every day!"
    elif month == 'march':
        challenge_text = "Learn django!"
    else:
        return HttpResponseNotFound("This month is not supported.")

    return HttpResponse(challenge_text)