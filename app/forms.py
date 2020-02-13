from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import PostAuthor

class PostAuthorCreationForm(UserCreationForm):

    class Meta:
        model = PostAuthor
        fields = ('username', 'email')

class PostAuthorChangeForm(UserChangeForm):

    class Meta:
        model = PostAuthor
        fields = ('username', 'email')
