from django.urls import path

from .views import AllProductView, DetailProductView, ActionView, \
    ListOurWorkView, Index, ContactsView, AboutCompanyView, DetailOurWorkView, Not_page, pdf_response

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('contact/', ContactsView.as_view(), name='contact'),
    path('about_company/', AboutCompanyView.as_view(), name='about_company'),
    path('action/', ActionView.as_view(), name='action'),
    path('our_works/', ListOurWorkView.as_view(), name='our_works'),
    path('our_work/<slug:slug>/', DetailOurWorkView.as_view(), name='detail_ourwork_view'),
    path('catalog/', AllProductView.as_view(), name='catalog'),
    path('catalog/product/<slug:slug>/', DetailProductView.as_view(), name='detail_product_view'),
    path('pdf/<slug:slug>', pdf_response, name='pdf_response'),
    path('not_page/', Not_page.as_view(), name='error'),

]


