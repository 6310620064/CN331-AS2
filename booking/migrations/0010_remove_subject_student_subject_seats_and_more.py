# Generated by Django 4.1.1 on 2022-10-06 15:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0009_alter_subject_quota_delete_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='student',
        ),
        migrations.AddField(
            model_name='subject',
            name='seats',
            field=models.ManyToManyField(blank=True, related_name='subjects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='subject',
            name='quota',
            field=models.PositiveIntegerField(default=0),
        ),
    ]