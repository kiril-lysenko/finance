# Generated by Django 4.1.3 on 2023-05-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_remove_moneybox_box_target_moneybox__box_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneybox',
            name='_box_target',
        ),
        migrations.AddField(
            model_name='moneybox',
            name='box_target',
            field=models.IntegerField(null=True, verbose_name='Конечная цель'),
        ),
    ]
