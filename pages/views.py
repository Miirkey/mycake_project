from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import servings_choices, price_choices,  city_choices


from listings.models import Listing
from bakers.models import Baker


def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    
    context = {

      'listings': listings,
      'servings_choices': servings_choices,
      'price_choices': price_choices,
      'city_choices': city_choices
    }

    return render(request, 'pages/index.html', context)


def about(request):

    bakers = Baker.objects.order_by('-hire_date')

    mvp_bakers = Baker.objects.all().filter(is_mvp=True)

    context = { 
        'bakers': bakers,
        'mvp_bakers': mvp_bakers
    }
    return render(request, 'pages/about.html', context)