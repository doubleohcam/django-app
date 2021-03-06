from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# dict for views
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

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # "<li><a href="...">January</a></li><li><a href="...">February</a></li>..."

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

# only accepts numbers
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # dynamic path
    return HttpResponseRedirect(redirect_path)

# only accepts strings
def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>" #injecting data/code/vars etc
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Value not supported!</h1>")