from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(label='Ваше имя',
                           max_length=25)
    email = forms.EmailField()
    to = forms.EmailField(label='Кому')
    comments = forms.CharField(label='Коментарий',
                               required=False,
                               widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Имя')
    body = forms.CharField(label='Коментарий',
                           widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

