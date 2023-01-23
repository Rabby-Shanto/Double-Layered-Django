from django import forms
from .models import Comment


class EmailSendForm(forms.Form):
    name = forms.CharField(max_length=25)
    from_email = forms.EmailField()
    to_email = forms.EmailField()
    message = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
