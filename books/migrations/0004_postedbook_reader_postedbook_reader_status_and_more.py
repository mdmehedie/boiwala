# Generated by Django 4.2.2 on 2023-07-18 04:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_book_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='postedbook',
            name='reader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reader', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='postedbook',
            name='reader_status',
            field=models.CharField(choices=[('Posted ', 'Posted'), ('Accept?', 'Accept?'), ('Accepted', 'Accepted'), ('Sent', 'Sent'), ('Sending', 'Sending'), ('Received', 'Received')], default='Posted', max_length=255),
        ),
        migrations.AddField(
            model_name='postedbook',
            name='requestor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='requestor', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postedbook',
            name='requestor_status',
            field=models.CharField(choices=[('Request Now', 'Request Now'), ('Requested', 'Requested'), ('Contract', 'Contract'), ('Received', 'Received'), ('Posted ', 'Posted')], default='Request Now', max_length=255),
        ),
        migrations.DeleteModel(
            name='RequestList',
        ),
    ]