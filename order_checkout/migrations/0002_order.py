# Generated by Django 4.1.1 on 2022-09-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_checkout', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ManyToManyField(to='order_checkout.item')),
            ],
        ),
    ]
