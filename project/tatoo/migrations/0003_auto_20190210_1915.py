# Generated by Django 2.1.5 on 2019-02-10 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatoo', '0002_auto_20190210_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='type',
            field=models.CharField(choices=[('w', 'Готовая работа'), ('s', 'Эскиз')], max_length=20),
        ),
    ]
