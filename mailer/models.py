from django.db import models

class EmailTemplate(models.Model):
    subject = models.TextField()
    body = models.TextField()
