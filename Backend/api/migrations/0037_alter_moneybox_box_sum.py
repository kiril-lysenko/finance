# Generated by Django 4.1.3 on 2023-05-12 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0036_alter_moneybox_box_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneybox',
            name='box_sum',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.outcomecash', verbose_name='Сумма накопления'),
        ),
    ]
