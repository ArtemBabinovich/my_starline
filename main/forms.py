from django import forms

from main.models import Comment, Feedback


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'phone', 'message')


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'message', 'text')
