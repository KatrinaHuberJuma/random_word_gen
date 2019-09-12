######### APP LEVEL views.py ########

from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "word_gen_app/index.html")

# Create your views here.
