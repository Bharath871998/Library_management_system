from django import forms
from .models import Book

# creating a form
class BookForm(forms.ModelForm):
    # create meta class
    class Meta:
        model = Book
        fields = [
            "name", "author", "price", "publish", "stock"
        ]
        
        
        
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'required': 'false'}),
            'publish': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'stock': forms.Select(attrs={'class': 'form-control', 'required': 'false'}),
        }
        # fields = "__all__"
        