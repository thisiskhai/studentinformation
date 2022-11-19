from django.forms import ModelForm
from .models import Forming

class ListingForm(ModelForm):
    class Meta:
        model = Forming
        fields = [
            'name',
            'phoneNumber',
            'className',
            'email',
            'note',
        ]