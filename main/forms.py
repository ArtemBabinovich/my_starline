from django import forms

from main.models import Comment, Feedback


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'numbers_phone', 'body')
        widgets = {'numbers_phone': forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': '+375 (29) 123-45-67',
        })}


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Иванов Иван Иванович'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'tel',
        'placeholder': '+375 (29) 123-45-67',
        }))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Хочу установить иммобилайзер и не потерять гарантию дилера'}))

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'message')

