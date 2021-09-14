from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import render

from . import models
from . import forms

# Create your views here.


def home(request):
    context = {}
    context['form']= forms.ModalForm()
    if request.method == 'GET':
        return render(request, 'home.html' ,context)
    elif request.method == 'POST':
        used_form = forms.ModalForm(request.POST)
        if used_form.is_valid():
            short_object = used_form.save()
            new_url = request.build_absolute_uri('/') + short_object.short_url
            long_url = short_object.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url
            return render(request, 'home.html', context)
        context['error'] = used_form.errors
        return render(request, "home.html", context)
    return render(request, "home.html")

def redirect_url_view(request, shortened_part):

    try:
        shortener = models.ShortUrl.objects.get(short_url=shortened_part)

        shortener.save()
        
        return HttpResponseRedirect(shortener.long_url)
        
    except:
        raise Http404('Sorry this link is broken :(')