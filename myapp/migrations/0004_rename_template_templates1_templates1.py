# Generated by Django 5.1.3 on 2025-01-24 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_templates1_delete_templates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='templates1',
            old_name='template',
            new_name='templates1',
        ),
    ]
