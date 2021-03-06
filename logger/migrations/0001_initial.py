# Generated by Django 3.2.1 on 2021-05-05 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Custom_Org',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=120)),
                ('action', models.CharField(max_length=120)),
                ('code', models.CharField(max_length=120)),
                ('name', models.CharField(max_length=120)),
                ('start_date', models.CharField(blank=True, max_length=120)),
                ('end_date', models.CharField(blank=True, max_length=120)),
                ('is_active', models.BooleanField()),
                ('department_code', models.CharField(blank=True, max_length=120)),
                ('template_code', models.CharField(blank=True, max_length=120)),
                ('semester_code', models.CharField(blank=True, max_length=120)),
                ('offering_code', models.CharField(blank=True, max_length=120)),
                ('custom_code', models.CharField(max_length=120)),
                ('classification', models.CharField(max_length=120)),
            ],
        ),
    ]
