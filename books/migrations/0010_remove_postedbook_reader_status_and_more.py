# Generated by Django 4.2.2 on 2023-07-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_postedbook_requestor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postedbook',
            name='reader_status',
        ),
        migrations.AddField(
            model_name='postedbook',
            name='book_position',
            field=models.CharField(choices=[('Posted Now', 'Posted Now'), ('Posted', 'Posted'), ('Request Now', 'Request Now'), ('Requested', 'Requested'), ('Accept?', 'Accept?'), ('Accepted', 'Accepted'), ('Contract', 'Contract'), ('Sending', 'Sending'), ('Sent', 'Sent'), ('Received', 'Received')], default='Posted Now', max_length=255),
        ),
    ]
