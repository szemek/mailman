from django import forms
from models import EmailTemplate

class EmailForm(forms.Form):
    email_templates = forms.ChoiceField(choices=EmailTemplate.objects.all())
    recipients = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=Recipient.objects.all()
    )
