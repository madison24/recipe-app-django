# Generated by Django 4.2.11 on 2024-05-06 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='directions',
            field=models.TextField(max_length=500),
        ),
    ]