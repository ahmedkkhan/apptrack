from django.shortcuts import render

from .models import Application


def index(request):
    applications = Application.objects.all().order_by('company')
    context = {
        'applications' : applications
    }

    return render(request, 'spreadsheet/index.html', context)