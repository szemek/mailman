from django.db import models

class EmailTemplate(models.Model):
    subject = models.TextField()
    body = models.TextField()

class Recipient(models.Model):
    name = models.TextField()
    email = models.EmailField()
