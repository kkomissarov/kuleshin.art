# Generated by Django 2.1.7 on 2019-02-15 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tatoo', '0003_auto_20190210_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zalupa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizda', models.CharField(max_length=20)),
                ('hui', models.TextField()),
            ],
        ),
    ]