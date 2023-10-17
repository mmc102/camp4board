from django import forms
from .models import Card, Comment

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['title', 'content', 'days_to_post']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content','username']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['username'].label = "Username (optional)"
        self.fields['content'].label = "Commentary"

