from django import forms
from django.contrib.auth.models import User
from .models import Friendship

class AddFriendForm(forms.Form):
    friend_username = forms.CharField(label='Friend Username', max_length=150)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_friend_username(self):
        username = self.cleaned_data['friend_username']
        try:
            friend = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError("User does not exist.")

        # Check if the friendship already exists
        if Friendship.objects.filter(user=self.user, friend=friend).exists():
            raise forms.ValidationError("You are already friends with this user.")
        if Friendship.objects.filter(user=friend, friend=self.user).exists():
            raise forms.ValidationError("You are already friends with this user.")

        return friend