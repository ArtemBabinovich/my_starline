from django.views.generic import CreateView

from main.forms import FeedbackForm


class GenericPhone(CreateView):
    form_class = FeedbackForm

    def get_form(self, form_class=None):
        self.object = super().get_form(form_class)
        return self.object

    def post(self, request, *args, **kwargs):
        form_class = FeedbackForm(request.POST)
        print(form_class)
        if len(form_class.data.get('phone')) > 18 and len(form_class.data.get('phone')) < 20:
            return self.form_valid(form_class)
        else:
            pass