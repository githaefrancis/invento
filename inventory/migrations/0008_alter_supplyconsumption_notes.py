# Generated by Django 4.0.3 on 2022-03-22 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_alter_equipment_equipment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplyconsumption',
            name='notes',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
