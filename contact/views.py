from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.


def contact(request):
    """ A view to send messages to the admin """
    if request.method == 'POST':
        contact = Contact()
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.firstname = firstname
        contact.lastname = lastname
        contact.email = email
        contact.message = message
        contact.save()
        messages.success(request, 'Thank you for your message! \
        We will get in touch as soon as possible.')
        return redirect('home')

    return render(request, 'contact/contact.html')
