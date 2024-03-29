# Generated by Django 4.2.2 on 2023-10-24 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='account/image/profile_img.png', upload_to='account/image/'),
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(choices=[('SSC', 'SSC'), ('HSC', 'HSC'), ('Graduation', 'Graduation'), ('Post Graduation', 'Post Graduation')], max_length=30)),
                ('passing_year', models.DateField()),
                ('institute', models.CharField(max_length=100)),
                ('board_or_university', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
