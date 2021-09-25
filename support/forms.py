from django import forms
from .models import *


class TicketForm(forms.ModelForm):
    title = forms.CharField(max_length=100, label='Enter the title', required=False)
    author = forms.CharField(max_length=50, label='How shall we name you?', required=True)
    text = forms.CharField(max_length=100, label='Descirbe you problem or ask a question',required=True, widget=forms.Textarea)

    class Meta:
        model = Ticket
        fields = ['title', 'author', 'text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name_comment', 'position_comment', 'text_comment']