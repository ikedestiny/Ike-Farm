from django import forms
from livestock.models import order

class contactUsForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)
    
class Customer_order_Form(forms.ModelForm):
    class Meta:
        model = order 
        fields = '__all__'