from django import forms
from django.core.exceptions import ValidationError

from bogis_nails.common.form_mixins import ReadonlyFieldsFormMixin
from bogis_nails.catalog.models import NailDesign


class NailDesignBaseForm(forms.ModelForm):                          

    class Meta:
        model = NailDesign
        fields = ('title', 'colors', 'size', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Nails title'}),
        }
        
        
class NailDesignCreateForm(NailDesignBaseForm):
    pass


class NailDesignEditForm(NailDesignBaseForm):
    readonly_fields = ('created_at',)
            
    def clean_created_at(self):
        # created_at = self.changed_data['created_at']
        # if created_at != self.instance.created_at:
        #     raise ValidationError('Created at is readonly!')
        
        return self.instance.created_at
        