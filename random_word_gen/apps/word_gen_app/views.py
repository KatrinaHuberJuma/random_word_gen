######### APP LEVEL views.py ########

from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def random_word(request):
    return render(request, "word_gen_app/index.html")

def generate(request):
    if request.method == "GET":
        return render(request, "word_gen_app/index.html")



# Create your views here.
