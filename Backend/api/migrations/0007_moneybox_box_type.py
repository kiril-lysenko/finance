# Generated by Django 4.1.3 on 2023-05-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_moneybox_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneybox',
            name='box_type',
            field=models.CharField(default='Накопления', max_length=50),
        ),
    ]
