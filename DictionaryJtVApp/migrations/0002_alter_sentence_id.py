# Generated by Django 4.2.3 on 2023-07-13 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DictionaryJtVApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]