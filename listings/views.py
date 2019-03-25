from django.shortcuts import render,get_object_or_404
from .models import Listing
from realtors.models import Realtor

def index(request):
     dynamic = Listing.objects.all()
     context = {
          'listings': dynamic
     }
     return render(request, 'listings/listings.html', context)

def listing(request,listing_id):
     listing=get_object_or_404(Listing, pk=listing_id)

     mvp_realtors=Realtor.objects.all().filter(is_mvp=True)

     context = {
          'listing': listing,
          'mvp_realtors':mvp_realtors
     }
     return render(request, 'listings/listing.html',context)


def search(request):
     query_list= Listing.objects.order_by('list_date')

     if 'city' in request.GET:
          city = request.GET['city']
          if city:
               query_list=query_list.filter(city__iexact=city)
     
     if 'keywords' in request.GET:
          keyword = request.GET['keywords']
          if keyword:
               query_list=query_list.filter(description__icontains=keyword)

     if 'state' in request.GET:
          state = request.GET['state']
          if state:
               query_list=query_list.filter(state__iexact=state)
     
     if 'bedrooms' in request.GET:
          bedrooms = request.GET['bedrooms']
          if bedrooms:
               query_list=query_list.filter(bedrooms__lte=bedrooms)

     if 'price' in request.GET:
          price = request.GET['price']
          if price:
               query_list=query_list.filter(price__lte=price)


     context={
          'listings': query_list
     }
     return render(request, 'listings/search.html', context)

