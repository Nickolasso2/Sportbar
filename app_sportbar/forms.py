from .models import BookedTable, SubscriptionContact
from django import forms
from captcha.fields import CaptchaField

class BookTableForm(forms.ModelForm):
    
    class Meta:
        model = BookedTable
        fields = ['datatime_booked', 'phone']
        widgets = {
            'datatime_booked':forms.DateTimeInput(attrs={'type':'datetime-local'}),
            'phone':forms.NumberInput(attrs={'type':'tel'})
            }
        

class SubscriptionForm(forms.ModelForm):
    captcha = CaptchaField()
    
    class Meta:
        model = SubscriptionContact
        fields= ['email']
        widgets = {
            'email':forms.EmailInput(attrs={'id':'form5Example21', 'class':'form-control'}),'captcha':forms.TextInput(attrs={'class':'form-control'})
        }