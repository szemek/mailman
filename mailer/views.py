from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from forms import EmailForm
from models import EmailTemplate, Recipient
from django.template import Context, Template
import sendgrid

class SendingView(View):
    template = 'mailer/sending_view.html'
    form_class = EmailForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # send emails
            recipients = form.cleaned_data['recipients']
            email_template = form.cleaned_data['email_template']

            recipients = Recipient.objects.filter(id__in=recipients)
            email_template = EmailTemplate.objects.get(id=email_template)

            EmailSender(recipients, email_template).deliver()

            return HttpResponseRedirect('')

        return render(request, self.template, {'form': form})

class EmailSender():
    def __init__(self, recipients, email_template):
        self.recipients = recipients
        self.email_template = email_template

    def deliver(self):
        sg = sendgrid.SendGridClient(SENDGRID_USERNAME, SENDGRID_PASSWORD)

        for recipient in self.recipients:
            message = sendgrid.Mail()
            message.add_to(recipient.email)
            message.set_subject(self.email_template.subject)
            template = Template(self.email_template.body)
            context = Context({'name': recipient.name})
            message.set_text(template.render(context))
            message.set_from('Przemek')
            status, msg = sg.send(message)
