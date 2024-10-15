from django import forms

from news.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']  # Удалите 'user' из полей
        widgets = {
            'message': forms.Textarea(
                attrs={'class': 'form-control', "rows": 3, "cols": 80, "placeholder": "Enter your message"})
        }
