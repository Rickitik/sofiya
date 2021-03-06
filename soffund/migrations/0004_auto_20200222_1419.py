# Generated by Django 3.0.3 on 2020-02-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soffund', '0003_auto_20200222_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='child',
            name='draft',
            field=models.BooleanField(default=True, verbose_name='Показ на сайте'),
        ),
        migrations.AlterField(
            model_name='child',
            name='money',
            field=models.PositiveSmallIntegerField(verbose_name='Необходимая сумма в долларах'),
        ),
    ]
