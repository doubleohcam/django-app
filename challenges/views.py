from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

monthly_challenges = {
    "january": "Eat your vegetables!",
    "february": "Walk every day!",
    "march": "Learn Django!",
    "april": "Eat your vegetables!",
    "may": "Walk every day!",
    "june": "Learn Django!",
    "july": "Eat your vegetables!",
    "august": "Walk every day!",
    "september": "Learn Django!",
    "october": "Eat your vegetables!",
    "november": "Walk every day!",
    "december": "Learn Django!",
}

# Create your views here.

# only accepts numbers
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
        
    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)

# only accepts strings
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("Value not supported!")