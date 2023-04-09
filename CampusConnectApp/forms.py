from django import forms
from .models import Users, Sell, Lost


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


class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        image = cleaned_data.get('image')
        description = cleaned_data.get('description')
        roll = cleaned_data.get('roll')

        # Perform validation checks on the form fields
        if not name:
            raise forms.ValidationError('Please enter a name')
        if not image:
            raise forms.ValidationError('Please input an image')
        if not description:
            raise forms.ValidationError('Please enter a description')
        if not roll:
            raise forms.ValidationError('Please enter a roll')

        # Return the cleaned data dictionary
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(LostForm, self).__init__(*args, **kwargs)
        self.fields['roll'].label_from_instance = lambda obj: "%s (%s)" % (
            obj.name, obj.roll)
