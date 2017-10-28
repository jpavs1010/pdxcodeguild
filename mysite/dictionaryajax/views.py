from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Dictionaryajax
import json


# Create your views here.

def index(request):
    return render(request, 'dictionaryajax/index.html', {})


def getwords(request):
    words = Dictionaryajax.objects.all()
    json_words = []
    for word in words:
        word_data = {}
        word_data['id'] = word.id
        word_data['word'] = word.word
        word_data['definition'] = word.definition
        json_words.append(word_data)
    return JsonResponse({'words': json_words})


def postwords(request):
    data = json.loads(request.body)
    item = Dictionaryajax(word=data['word'], definition=data['definition'])
    item.save()
    return HttpResponse('ok')






