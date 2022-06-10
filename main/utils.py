
from django.views.generic.edit import FormMixin, ModelFormMixin

from main.forms import FeedbackForm
from main.telegram_bot import dialogue


class GenericPhone(ModelFormMixin):

    form_class = FeedbackForm

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def post(self, request, *args, **kwargs):
        form_class = FeedbackForm(request.POST)
        print(form_class.data)
        return self.form_valid(form_class)

    def form_valid(self, form_class):
        try:
            form_class.save()
            dialogue(form_class.data['phone'].replace(' ', ''), form_class.data['name'], form_class.data['message'])
            return super().form_valid(form_class)
        except:
            dialogue(form_class.data['phone'].replace(' ', ''), '', '')
            return super().form_valid(form_class)


class GenericPhone1(FormMixin):
    form_class = FeedbackForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form_class = FeedbackForm(request.POST)
        return self.form_valid(form_class)

    def form_valid(self, form_class):
        try:
            form_class.save()
            print(form_class.cleaned_data)
            dialogue(form_class.data['phone'].replace(' ', ''), form_class.data['name'], form_class.data['message'])
            return super().form_valid(form_class)
        except:
            dialogue(form_class.data['phone'].replace(' ', ''), '', '')
            return super().form_valid(form_class)
