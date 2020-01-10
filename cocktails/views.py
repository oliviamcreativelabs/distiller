from django.shortcuts import render

from . models import Cocktail


def index(request):  
    cocktails = Cocktail.objects.all()

    context = {
        'cocktails': cocktails
    }

    # Bring in info by using a dictionary
    return render(request, 'cocktails/cocktails.html', context)


def cocktail(request):
    return render(request, 'cocktails/cocktail.html')


def search(request):
    return render(request, 'cocktails/search.html')
