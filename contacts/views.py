from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['listing_id']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
                
                if has_contacted:
                        messages.error(request, 'You have already made an inquiry for this listing')
                contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, 
                            message=message, user_id=user_id)
                contact.save()
                send_mail(
                        'Property Listing Inquiry',
                        'There has been an inquiry for ' + listing + '. Sign into the admin for more info',
                        'gauravusadadiya1998@gmail.com',
                        [realtor_email, 'gauravusadadiya1998@gmail.com']
                )
                messages.success(request, 'Your request has been submited')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, 
                            message=message, user_id=user_id)

        contact.save()

        send_mail(
                'Property Listing Inquiry',
                'There has been an inquiry for ' + listing + '. Sign into the admin for more info',
                 'gauravusadadiya1998@gmail.com',
                 [realtor_email, 'gauravusadadiya1998@gmail.com']
        )

        messages.success(request, 'Your request has been submited')

        return redirect('/listings/'+listing_id)
        
