from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Contact
from django.urls import reverse
from twilio.rest import Client

# Create your views here.


def index(request):
    names = Contact.objects.all()
    context = {'names': names}
    return render(request, 'contactlist/index.html', context)


def detail(request, name_id):
    name = get_object_or_404(Contact, pk=name_id)
    return render(request, 'contactlist/detail.html', {'name': name})


def add(request):
    name_entry = request.POST['name_entry']
    phone_number = request.POST['phone_number']
    favorite_color = request.POST['favorite_color']
    favorite_fruit = request.POST['favorite_fruit']
    catch_phrase = request.POST['catch_phrase']
    contact_entry = Contact(name=name_entry, phone_number=phone_number, favorite_color=favorite_color, favorite_fruit=favorite_fruit,catch_phrase=catch_phrase)
    contact_entry.save()
    return HttpResponseRedirect(reverse('contactlist:index'))


def sms(request):
    id = request.POST['id']
    contact = Contact.objects.get(pk=id)
    print(contact.phone_number)
    print(request.POST['sms_text'])
    account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxx'
    auth_token = 'xxxxxxxxxxxxxxxxxxxxxxx'
    client = Client(account_sid, auth_token)
    message = client.api.account.messages.create(
        to= contact.phone_number,
        from_="+xxxxxxxxxxx",
        body=request.POST['sms_text'])

    return HttpResponseRedirect(reverse('contactlist:index'))


