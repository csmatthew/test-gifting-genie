from django.shortcuts import render
from .models import MyAccount
from django.contrib.auth.decorators import login_required
from wishlist.models import WishlistItem

@login_required
def profile_view(request):
    myaccount, created = MyAccount.objects.get_or_create(user=request.user)
    return render(request, 'myaccount/profile.html', {'myaccount': myaccount})

@login_required
def user_wishlist_view(request):
    myaccount, created = MyAccount.objects.get_or_create(user=request.user)
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'myaccount': myaccount, 'wishlist_items': wishlist_items})
