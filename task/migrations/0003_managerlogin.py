# Generated by Django 3.2.4 on 2021-06-28 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManagerLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=520)),
                ('password', models.CharField(max_length=250)),
            ],
        ),
    ]
