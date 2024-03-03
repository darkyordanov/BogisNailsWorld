from django import forms

from bogis_nails.product.models import Product


class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ('title', 'description', 'price', 'quantity', 'image')
        
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Product title'}),
            'description': forms.TextInput(attrs={'placeholder': 'Product description'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Product price'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Product Quantity'}),
            'image': forms.FileInput(attrs={'placeholder': 'Product image'}),
        }
        
       
