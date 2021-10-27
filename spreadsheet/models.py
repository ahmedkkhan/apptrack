from django.db import models


class Application(models.Model):
    company = models.CharField(max_length=50)
    application_date = models.DateField()

    APPLICATION_STATUS_CHOICES = [
        ('Waiting', 'Waiting for response'),
        ('Received OA', 'Received online assessment'),
        ('Completed OA', 'Completed online assessment'),
        ('Received interview', 'Received interview'),
        ('Completed interview', 'Completed interview'),
        ('Received offer', 'Received offer'),
        ('Rejected', 'Rejected'),
        ('Ghosted', 'Ghosted'),
    ]
    application_status = models.CharField(
        choices=APPLICATION_STATUS_CHOICES,
        default='N',
        max_length=30,
    )