from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponseRedirect
from forms import EmailForm

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
            return HttpResponseRedirect('')

        return render(request, self.template, {'form': form})
