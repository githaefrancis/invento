# Generated by Django 4.0.3 on 2022-03-22 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_alter_allocation_date_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allocation',
            name='notes',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
