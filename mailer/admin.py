from django.contrib import admin

from models import EmailTemplate
from models import Recipient

admin.site.register(EmailTemplate)
admin.site.register(Recipient)
