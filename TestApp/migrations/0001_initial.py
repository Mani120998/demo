# Generated by Django 4.2.19 on 2025-03-04 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentname', models.TextField(blank=True, null=True)),
                ('standard', models.TextField(blank=True, null=True)),
                ('section', models.TextField(blank=True, null=True)),
                ('grade', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
