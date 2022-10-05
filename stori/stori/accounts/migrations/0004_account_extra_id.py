# Generated by Django 3.2.10 on 2022-10-04 19:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_transactions_oncredit'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='extra_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]