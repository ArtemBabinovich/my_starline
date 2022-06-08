
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Contacts, Product, Company, Action, Sale, OurWork
from .utils import GenericPhone


class Index(ListView, GenericPhone):
    """Главная"""
    model = Contacts
    template_name = 'starline/index.html'
    context_object_name = 'contact'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.count()
        return context


class ContactsView(ListView, GenericPhone):
    """Контакты и информация"""
    model = Contacts
    template_name = 'starline/contact.html'
    context_object_name = 'contact'


class AboutCompanyView(ListView, GenericPhone):
    """О компании"""
    model = Company
    template_name = 'starline/about_company.html'
    context_object_name = 'company'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()
        return context


class ActionView(ListView, GenericPhone):
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
        return context


class ListOurWorkView(ListView, GenericPhone):
    """Список портфолио"""
    model = Contacts
    template_name = 'starline/portfolio_all.html'
    context_object_name = 'contact'


class DetailOurWorkView(DetailView):
    """Детализация портфолио"""
    model = OurWork
    template_name = 'starline/portfolio_card.html'
    context_object_name = 'ourwork'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.count()
        context['contact'] = Contacts.objects.all()
        return context


class AllProductView(ListView, GenericPhone):
    """Вывод продуктов на экран"""
    model = Contacts
    template_name = 'starline/catalog.html'
    context_object_name = 'contact'


class DetailProductView(DetailView):
    """Детализация продукта"""
    model = Product
    template_name = 'starline/product_page.html'
    context_object_name = 'prod'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contacts.objects.all()
        context['products'] = Product.objects.count()
        return context


def pdf_response(request, id):
    try:
        obj = Product.objects.get(id=id)
        return FileResponse(open('media/'+str(obj.instruction), 'rb'))
    except BaseException as e:
        return render(request, 'starline/product_page.html')


class Not_page(ListView, GenericPhone):
    model = Contacts
    template_name = '404.html'
    context_object_name = 'contact'


def error(request, exception):
    contacts = Contacts.objects.all()
    return render(request, '404.html', {'contact': contacts}, status=404)
