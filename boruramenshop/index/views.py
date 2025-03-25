from django.shortcuts import render, redirect
from django.utils.translation import activate
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _

def main(request):
    return render(request, 'main.html')

def menu(request):
    categories = [
        {"name": _("Przystawki"), "anchor": "Przystawki"},
        {"name": _("Dania główne"), "anchor": "Dania_glowne"},
        {"name": _("Ramen"), "anchor": "Ramen"},
        {"name": _("Dodatki"), "anchor": "Dodatki"},
        {"name": _("Desery"), "anchor": "Desery"},
        {"name": _("Napoje"), "anchor": "Napoje"},
        {"name": _("Alkohole"), "anchor": "Alkohole"},
    ]
    return render(request, "menu.html", {"categories": categories})

def PolitykaStrony(request):
    return render(request, 'polityka_strony.html')


def set_language(request):
    lang = request.GET.get('lang') 
    if lang in ['pl', 'en']: 
        request.session['language'] = lang  
        activate(lang) 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))  # Powrót na poprzednią stronę
