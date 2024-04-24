from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # display article list
    return render(request, "blog/index.html", {})


def article_detail(request, article_id):
    return HttpResponse(f"article: {article_id}")
