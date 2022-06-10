from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import FeedbackForm, CommentForm
from .models import Contacts, Product, Company, Action, Sale, OurWork
from .telegram_bot import dialogue, review
from .utils import GenericPhone1


class Index(ListView, GenericPhone1):
    """Главная"""
    model = Contacts
    template_name = 'starline/index.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.count()
        context['form'] = self.get_form()
        return context


def index(request):
    """Главная"""
    contact = Contacts.objects.all()
    products = Product.objects.count()
    context = {'contact': contact, 'products': products}
    if request.method == 'POST':
        form_number = FeedbackForm(request.POST)
        form_message = CommentForm(request.POST)
        if 'message' in request.POST != '':
            if form_message.is_valid():
                form_message.save()
                review(
                    form_message.data['phone'].replace(' ', ''),
                    form_message.data['name'],
                    form_message.data['message'],
                )
                return render(request, 'starline/index.html', context)
        if 'name' in request.POST and 'text' in request.POST:
            if form_number.is_valid():
                form_number.save()
                dialogue(
                    form_number.data['phone'].replace(' ', ''),
                    form_number.data['name'],
                    form_number.data['text'],
                    '',
                )
                return render(request, 'starline/index.html', context)
        if 'name' in request.POST != '':
            if form_number.is_valid():
                form_number.save()
                dialogue(form_number.data['phone'].replace(' ', ''),
                         form_number.data['name'],
                         '',
                         '',
                         )
                return render(request, 'starline/index.html', context)
        if 'phone' in request.POST:
            if form_number.is_valid():
                form_number.save()
                if form_number.data['phone']:
                    dialogue(form_number.data['phone'].replace(' ', ''), '', '', '')
                    return render(request, 'starline/index.html', context)

        return render(request, 'starline/index.html', context)
    return render(request, 'starline/index.html', context)


class ContactsView(ListView, GenericPhone1):
    """Контакты и информация"""
    model = Contacts
    template_name = 'starline/contact.html'
    context_object_name = 'contact'


class AboutCompanyView(ListView, GenericPhone1):
    """О компании"""
    model = Company
    template_name = 'starline/about_company.html'
    context_object_name = 'company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()
        context['form'] = self.get_form()
        return context


class ActionView(ListView, GenericPhone1):
    """Вывод акций на экран"""
    model = Action
    template_name = 'starline/action.html'
    context_object_name = 'action'

    def get_queryset(self):
        return Action.objects.filter(published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()
        context['sale'] = Sale.objects.filter(published=True)
        context['form'] = self.get_form()
        return context


def action(request):
    """Вывод акций на экран"""
    action = Action.objects.filter(published=True)
    contact = Contacts.objects.all()
    sale = Sale.objects.filter(published=True)
    context = {'action': action, 'contact': contact, 'sale': sale}

    if request.method == 'POST':
        form_number = FeedbackForm(request.POST)
        form_message = CommentForm(request.POST)
        if 'message' in request.POST != '':
            if form_message.is_valid():
                form_message.save()
                review(
                    form_message.data['phone'].replace(' ', ''),
                    form_message.data['name'],
                    form_message.data['message'],
                )
                return render(request, 'starline/action.html', context)

        if 'name' in request.POST != '':
            if form_number.is_valid():
                form_number.save()
                dialogue(form_number.data['phone'].replace(' ', ''),
                         form_number.data['name'],
                         '',
                         '',
                         )
                return render(request, 'starline/action.html', context)

        return render(request, 'starline/action.html', context)
    return render(request, 'starline/action.html', context)


class ListOurWorkView(ListView, GenericPhone1):
    """Список портфолио"""
    model = Contacts
    template_name = 'starline/portfolio_all.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class DetailOurWorkView(DetailView, GenericPhone1):
    """Детализация портфолио"""
    model = OurWork
    template_name = 'starline/portfolio_card.html'
    context_object_name = 'ourwork'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.count()
        context['contact'] = Contacts.objects.all()
        context['form'] = self.get_form()
        return context


class AllProductView(ListView, GenericPhone1):
    """Вывод продуктов на экран"""
    model = Contacts
    template_name = 'starline/catalog.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


class DetailProductView(GenericPhone1, DetailView):
    """Детализация продукта"""
    model = Product
    template_name = 'starline/product_page.html'
    context_object_name = 'prod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()
        context['products'] = Product.objects.count()
        context['form'] = self.get_form()
        return context


def pdf_response(request, slug):
    try:
        obj = Product.objects.get(slug=slug)
        return FileResponse(open('media/' + str(obj.instruction), 'rb'))
    except BaseException as e:
        return render(request, 'starline/product_page.html')


class Not_page(ListView, GenericPhone1):
    model = Contacts
    template_name = '404.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


def error(request, exception):
    contact = Contacts.objects.all()
    return render(request, '404.html', {'contact': contact}, status=404)
