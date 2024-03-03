from django import forms

from bogis_nails.product.models import Product


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Product title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Product description'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Product price'}),
            'image': forms.FileInput(attrs={'placeholder': 'Product image'}),
        }
        
       
