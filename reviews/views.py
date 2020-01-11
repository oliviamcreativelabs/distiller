from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Review, Whiskey
from .forms import ReviewForm
import datetime
from .models import Review, Whiskey

'''
We have defined four different views (one for each of the four different url mappings). 
Each function gets at least a request object parameter, and optionally more parameters as specified in the url mapping. For example, the review_detail function gets also a review_id parameter as we specified in the mapping.
'''


def review(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/reviews.html', context)


#  =====================================================
# gets a list of the latest 9 reviews and renders it using `reviews/list.html'.


def review_list(request):
    # ℹ Queries are performed by using the .objects attribute.
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list': latest_review_list}
    return render(request, 'reviews/review_list.html', context)


#  =====================================================
# gets a review given its ID and renders it using review_detail.html.

def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})


#  =====================================================
# gets all the whiskey sorted by name and passes it to Whiskey_list.html to be rendered.

def whiskey_list(request):
    # ℹ
    whiskey_list = Whiskey.objects.order_by('-name')
    context = {'whiskey_list': whiskey_list}
    return render(request, 'reviews/whiskey_list.html', context)


#  =====================================================
# gets whiskey from DB given its ID and renders it using whiskey_detail.html.

def whiskey_detail(request, whiskey_id):
    whiskey = get_object_or_404(Whiskey, pk=whiskey_id)
    return render(request, 'reviews/whiskey_detail.html', {'whiskey': whiskey, 'form': form})


'''
The add_review function is in charge of validating the form and creating the new review instance. The first thing it does is to use the request url whiskey ID to look for the whiskey we are going to add the review to. It will redirect the view to a 404 page if it doesn't find it. Otherwise, it will create a ReviewForm instance from the request POST data).
'''


def add_review(request, wine_id):
    whiskey = get_object_or_404(whiskey, pk=whiskey_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.whiskey = whiskey
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('reviews:whiskey_detail', args=(whiskey.id,)))

    return render(request, 'reviews/wine_detail.html', {'wine': wine, 'form': form})
