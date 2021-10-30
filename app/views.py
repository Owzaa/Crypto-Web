"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )


def refferals(request):
    """Renders the refferals page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/refferals.html',
        {
            'title':'Refferals',
            'message':'Refferal Guides.',
            'year':datetime.now().year,
        }
    )



def cryptoStockvel(request):
    """Renders the cryptoStockvel page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/crypto-stockvel.html',
        {
            'title':'Crypto-Stockvel',
            'message':'Crypto-Stockvel Guideline.',
            'year':datetime.now().year,
        }
    )

def markets(request):
    """Renders the markets page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/markets.html',
        {
            'title':'The - Markets',
            'message':'Crypto-Stockvel Markets',
            'year':datetime.now().year,
        }
    )

def tradings(request):
    """Renders the tradings page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/tradings.html',
        {
            'title':'Trading / Mining',
            'message':'Trading / Mining via ( Crypto - Stockvel )',
            'year':datetime.now().year,
        }
    )

def portfolio(request):
    """Renders the Portfolio page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/portfolio.html',
        {
            'title':'Portfolio ',
            'message':'Create your Market Portfolio with Crypto - Stockvel | RSA',
            'year':datetime.now().year,
        }
    )
