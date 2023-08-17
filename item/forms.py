from django import forms
from .models import Item

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category','name','description','price','image')

        INPUT_CLASSESS='w-full py-4 py-6 rounded-xl border'
        widgets={
            'category':forms.Select(attrs={
                'class':'w-full py-4 py-6 rounded-xl border'
            }),
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSESS

            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSESS
                
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSESS
                
            })
        }



class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','price','image','is_sold')

        INPUT_CLASSESS='w-full py-4 py-6 rounded-xl border'
        widgets={
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSESS

            }),
            'description':forms.Textarea(attrs={
                'class':INPUT_CLASSESS
                
            }),
            'price':forms.TextInput(attrs={
                'class':INPUT_CLASSESS
                
            }),
            'image':forms.FileInput(attrs={
                    'class':INPUT_CLASSESS
            })
        }