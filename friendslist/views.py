from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Friendship
from .forms import AddFriendForm
from django.http import JsonResponse

def search_usernames(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('term', '')
        users = User.objects.filter(username__icontains=query)
        results = [user.username for user in users]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)


def friendship_list(request):
    friendships = Friendship.objects.filter(user=request.user, confirmed=True)
    pending_friendships = Friendship.objects.filter(friend=request.user, confirmed=False)
    if request.method == 'POST':
        form = AddFriendForm(request.POST, user=request.user)
        if form.is_valid():
            friend = form.cleaned_data['friend_username']
            Friendship.objects.create(user=request.user, friend=friend)
            return redirect('friendslist')
    else:
        form = AddFriendForm(user=request.user)
    return render(request, 'friendslist/friendslist.html', {'friendships': friendships, 'pending_friendships': pending_friendships, 'form': form})

class FriendshipListView(ListView):
    model = Friendship
    template_name = 'friendslist/friendslist.html'
    context_object_name = 'friendships'

    def get_queryset(self):
        return Friendship.objects.filter(user=self.request.user, confirmed=True)

def confirm_friendship(request, friendship_id):
    friendship = get_object_or_404(Friendship, id=friendship_id, friend=request.user)
    if request.method == 'POST':
        friendship.confirmed = True
        friendship.save()
        return HttpResponseRedirect(reverse('friendslist'))