from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact


# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing = request.POST['listing']
        listing_id = request.POST['listing_id']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        new_contact = Contact(listing=listing, listing_id=listing_id, name=name,
                              email=email, phone=phone, message=message, user_id=user_id)
        new_contact.save()

        messages.success(request, "You've Successfully made an inquiry. "
                                  "We will get back to you soon")

        return redirect('/listings/' + listing_id)