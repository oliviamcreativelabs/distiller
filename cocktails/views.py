from django.shortcuts import render


def index(request):
    return render(request, 'cocktails/cocktails.html')


def cocktail(request):
    return render(request, 'cocktails/cocktail.html')


def search(request):
    return render(request, 'cocktails/search.html')
