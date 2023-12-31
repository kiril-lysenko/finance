# Generated by Django 4.1.3 on 2023-05-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_moneybox_box_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneybox',
            name='box_target',
            field=models.IntegerField(null=True, verbose_name='Конечная цель'),
        ),
        migrations.AlterField(
            model_name='moneybox',
            name='box_name',
            field=models.CharField(max_length=255, verbose_name='Название накопления'),
        ),
        migrations.AlterField(
            model_name='moneybox',
            name='box_sum',
            field=models.IntegerField(verbose_name='Сумма накопления'),
        ),
    ]
