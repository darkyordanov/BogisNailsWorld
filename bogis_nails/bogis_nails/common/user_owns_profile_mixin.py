from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import UserPassesTestMixin

from bogis_nails.account.models import Profile


class UserOwnsProfileMixin(UserPassesTestMixin):
    def test_func(self):
        # Retrieve the profile ID from the URL parameters
        profile_id = self.kwargs.get('pk')
        
        # Retrieve the requested profile object
        profile = get_object_or_404(Profile, pk=profile_id)
        
        # Check if the requested profile belongs to the currently logged-in user
        return profile.user == self.request.user
    
