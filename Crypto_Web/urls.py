"""
Definition of urls for Crypto_Web.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
  path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('refferals/', views.refferals, name='refferals'),
    path('cryptoStockvel/', views.cryptoStockvel, name='cryptoStockvel'),

    path('markets/',views.markets, name='markets'),
    path('tradings/',views.tradings, name='tradings'),
    path('portfolio/',views.portfolio, name='portfolio'),

    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': ' Crypto - Stockvel (Log-in)',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
