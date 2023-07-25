# Generated by Django 4.2.2 on 2023-07-25 05:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0005_alter_postedbook_reader_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postedbook',
            name='reader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reader', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postedbook',
            name='requestor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='requestor', to=settings.AUTH_USER_MODEL),
        ),
    ]