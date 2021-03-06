# Generated by Django 3.2.8 on 2021-10-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spreadsheet', '0002_alter_application_application_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_status',
            field=models.CharField(choices=[('Waiting', 'Waiting for response'), ('Received OA', 'Received online assessment'), ('Completed OA', 'Completed online assessment'), ('Received interview', 'Received interview'), ('Completed interview', 'Completed interview'), ('Received offer', 'Received offer'), ('Rejected', 'Rejected'), ('Ghosted', 'Ghosted')], default='N', max_length=30),
        ),
    ]
