# Generated by Django 4.2.3 on 2023-07-25 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('DictionaryJtVApp', '0007_alter_customeruser_password'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customeruser',
            options={'permissions': (('custom_groups', 'Custom groups'), ('custom_user_permissions', 'Custom user permissions'))},
        ),
        migrations.AddField(
            model_name='customeruser',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='custom_user', to='auth.group'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='customeruser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='custom_user_set', related_query_name='custom_user', to='auth.permission'),
        ),
    ]