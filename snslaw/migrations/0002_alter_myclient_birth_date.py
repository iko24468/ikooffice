# Generated by Django 4.1.3 on 2023-02-17 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snslaw', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclient',
            name='birth_date',
            field=models.DateField(verbose_name='תאריך לידה'),
        ),
    ]
