
from django.views.generic.edit import FormMixin

from main.forms import FeedbackForm
from main.telegram_bot import dialogue


class GenericPhone1(FormMixin):
    form_class = FeedbackForm
    success_url = '/'

    def post(self, request):
        form_class = FeedbackForm(request.POST)
        print(form_class.data)
        return self.form_valid(form_class)

    def form_valid(self, form_class):
        form_class.save()
        try:
            if form_class.data['text']:
                dialogue(form_class.data['phone'].replace(' ', ''),
                         form_class.data['name'],
                         form_class.data['text'],
                         '',
                         )
                return super().form_valid(form_class)
            if form_class.data['name']:
                dialogue(form_class.data['phone'].replace(' ', ''), form_class.data['name'], '', '')
                return super().form_valid(form_class)
            if form_class.data['phone']:
                dialogue(form_class.data['phone'].replace(' ', ''), '', '', '')
                return super().form_valid(form_class)
        except:
            if form_class.data['message']:
                dialogue(form_class.data['phone'].replace(' ', ''),
                         form_class.data['name'],
                         form_class.data['message'],
                         '',
                         )
                return super().form_valid(form_class)
            if form_class.data['name']:
                dialogue(form_class.data['phone'].replace(' ', ''), form_class.data['name'], '', '')
                return super().form_valid(form_class)
            if form_class.data['phone']:
                dialogue(form_class.data['phone'].replace(' ', ''), '', '', '')
                return super().form_valid(form_class)
