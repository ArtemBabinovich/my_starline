
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .forms import FeedbackForm
from .models import Contacts, Product, Company, Action, Sale, OurWork
from .utils import GenericPhone, GenericPhone1


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


class ContactsView(ListView, GenericPhone1):
    """Контакты и информация"""
    model = Contacts
    template_name = 'starline/contact.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context


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


class DetailProductView(DetailView, GenericPhone1):
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


def pdf_response(request, id):
    try:
        obj = Product.objects.get(slug=id)
        return FileResponse(open('media/'+str(obj.instruction), 'rb'))
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
