# Generated by Django 4.1.1 on 2022-10-06 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_subject_academic_year_alter_subject_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='quota',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
