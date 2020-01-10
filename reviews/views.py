from django.shortcuts import get_object_or_404, render

from .models import Review, Whiskey

'''
We have defined four different views (one for each of the four different url mappings). 
Each function gets at least a request object parameter, and optionally more parameters as specified in the url mapping. For example, the review_detail function gets also a review_id parameter as we specified in the mapping.
'''


def review_list(request):
    # ℹ Queries are performed by using the .objects attribute.
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/review_list.html', context)


def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


def whiskey_list(request):
    # ℹ
    whiskey_list = Whiskey.objects.order_by('-name')
    context = {'whiskey_list': whiskey_list}
    return render(request, 'reviews/whiskey_list.html', context)


def whiskey_detail(request, whiskey_id):
    whiskey = get_object_or_404(whiskey, pk=whiskey_id)
    return render(request, 'reviews/whiskey_detail.html', {'whiskey': whiskey})