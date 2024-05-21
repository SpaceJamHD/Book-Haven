from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']
        labels = {
            'text': 'Залиште коментарій',
            'rating': 'Оцінка'
        }
        widgets = {
            'rating': forms.Select(choices=[(i, str(i)) for i in range(1, 6)])
        }

class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск', max_length=100, required=False)