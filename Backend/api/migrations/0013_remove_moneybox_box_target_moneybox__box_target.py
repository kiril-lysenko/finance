# Generated by Django 4.1.3 on 2023-05-06 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_remove_moneybox__box_target_moneybox_box_target'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moneybox',
            name='box_target',
        ),
        migrations.AddField(
            model_name='moneybox',
            name='_box_target',
            field=models.IntegerField(editable=False, null=True, verbose_name='Конечная цель'),
        ),
    ]
