from django import forms
from .models import Users, Sell


class UserForm(forms.ModelForm):
    class Meta:
        model = Users
        exclude = ['username', 'password']


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        exclude = ['id', 'sold']

    def __init__(self, *args, **kwargs):
        super(SellForm, self).__init__(*args, **kwargs)
        self.fields['roll'].label_from_instance = lambda obj: "%s (%s)" % (
            obj.name, obj.roll)
