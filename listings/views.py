from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from .models import Listing
from .choices import states_choices, price_choices, bedroom_choices


# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {'listings': paged_listings}
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    the_listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': the_listing
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_published=True)
    if 'keywords' in request.GET and request.GET['keywords']:
        keywords = request.GET['keywords']
        queryset_list = queryset_list.filter(description__contains=keywords)

    if 'city' in request.GET and request.GET['city']:
        city = request.GET['city']
        queryset_list = queryset_list.filter(city__iexact=city)

    if 'state' in request.GET and request.GET['state']:
        state = request.GET['state']
        queryset_list = queryset_list.filter(state__iexact=state)

    if 'bedrooms' in request.GET and request.GET['bedrooms']:
        bedrooms = request.GET['bedrooms']
        queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET and request.GET['price']:
        price = request.GET['price']
        queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'listings': queryset_list,
        'states_choices': states_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)