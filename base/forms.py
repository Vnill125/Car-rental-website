from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order, Contact
from django import forms

from django.utils.timezone import now

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1','password2','email']
        
    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control', 'placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class':'form-control', 'placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'form-control', 'placeholder':'Password confirmation'})
        self.fields['email'].widget.attrs.update({'class':'form-control', 'placeholder':'user@gmail.com'})

class DateInput(forms.DateInput):
    input_type = 'date'
    
    def get_context(self, name, value, attrs):
        attrs.setdefault('min', now().strftime('%Y-%m-%d'))
        return super().get_context(name, value, attrs)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['contact_phone','startRent','endRent','pickUp']
        widgets = {
            'startRent': DateInput(),
            'endRent': DateInput()
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contact_phone'].widget.attrs.update({'class':'form-control', 'placeholder':'+48 000 999 888'})
        self.fields['startRent'].widget.attrs.update({'class':'form-control'})
        self.fields['endRent'].widget.attrs.update({'class':'form-control'})
        self.fields['pickUp'].widget.attrs.update({'class':'form-control'})
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class':'form-control'})
        self.fields['email'].widget.attrs.update({'class':'form-control'})
        self.fields['subject'].widget.attrs.update({'class':'form-control'})
        self.fields['message'].widget.attrs.update({'class':'form-control'})