from django import forms
from models import EmailTemplate
from models import Recipient

class EmailForm(forms.Form):
    email_templates = forms.ChoiceField(choices=[(email.id, email.subject) for email in EmailTemplate.objects.all()] )
    recipients = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=[(recipient.id, recipient.name) for recipient in Recipient.objects.all()]
    )
