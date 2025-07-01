from django import forms
import datetime

from catalog.models import BookInstance

class RenewBookForm(forms.ModelForm):
    due_back = forms.DateField(
        help_text="Enter a date between now and 4 weeks (default 3).",
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )

    class Meta:
        model = BookInstance
        fields = ['due_back']

    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Check if date is not in past
        if data < datetime.date.today():
            raise forms.ValidationError('Invalid date - renewal in past')

        # Check if date is within allowed range (+4 weeks)
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise forms.ValidationError('Invalid date - more than 4 weeks ahead')

        return data
