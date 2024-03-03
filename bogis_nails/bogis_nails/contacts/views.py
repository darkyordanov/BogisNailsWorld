from django.shortcuts import render

from bogis_nails.contacts.models import ArtistContacts


def contacts(request):
    artist_contacts = ArtistContacts.objects.first()
    
    context = {
        'phone_number': artist_contacts.phone_number,
        'email': artist_contacts.email,
        'address': artist_contacts.address,
    }
    
    return render(request, 'contacts/contacts.html', context)


