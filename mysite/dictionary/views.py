from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dictionary
from django.urls import reverse

# Create your views here.


def index(request):
    words = Dictionary.objects.all()
    context = {'words': words}
    return render(request, 'dictionary/index.html', context)


def detail(request, word_id):
    word = get_object_or_404(Dictionary, pk=word_id)
    return render(request, 'dictionary/detail.html', {'word': word})


def add(request):
    word_entry = request.POST['word_entry']
    definition_entry = request.POST['definition_entry']
    dictionary_entry = Dictionary(word=word_entry, definition=definition_entry)
    dictionary_entry.save()

    return HttpResponseRedirect(reverse('dictionary:index'))

def delete (request):
    pass


