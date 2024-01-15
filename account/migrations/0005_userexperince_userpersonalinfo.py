# Generated by Django 5.0.1 on 2024-01-15 05:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_userskill'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExperince',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_name', models.CharField(max_length=100)),
                ('job_role', models.CharField(max_length=200)),
                ('exprince', models.IntegerField()),
                ('do_join', models.DateField()),
                ('do_resign', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserPersonalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1)),
                ('dob', models.DateField()),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]