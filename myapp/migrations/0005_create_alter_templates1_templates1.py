# Generated by Django 5.1.3 on 2025-01-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_template_templates1_templates1'),
    ]

    operations = [
        migrations.CreateModel(
            name='create',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.AlterField(
            model_name='templates1',
            name='templates1',
            field=models.FileField(upload_to='files/'),
        ),
    ]
