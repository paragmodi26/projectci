# Generated by Django 3.2.4 on 2021-06-30 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_auto_20210630_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='footer',
            name='footer',
        ),
        migrations.AddField(
            model_name='footer',
            name='address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='contact_number',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='footer',
            name='email_id',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
