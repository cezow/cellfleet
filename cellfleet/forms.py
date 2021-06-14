from django import forms
from .models import MobileNumber


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MobileNumberForm(forms.ModelForm):

    class Meta:
        model = MobileNumber
        # fields = '__all__'
        fields = ('number', 'sim', 'pin', 'puk', 'tariff', 'employee')
        labels = {
            'number': 'Mobile',
            'tariff': 'Tariff',
            'sim': 'SIM',
            'pin': 'PIN',
            'puk': 'PUK',
            'employee': 'Employee'
        }
    
    def __init__(self, *args, **kwargs):
        super(MobileNumberForm, self).__init__(*args, **kwargs)
        self.fields['employee'].empty_label = ''
        self.fields['employee'].required = False

