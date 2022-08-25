# Generated by Django 4.1 on 2022-08-17 08:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('citizen_id', models.PositiveBigIntegerField(verbose_name='citizen_id')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.PositiveBigIntegerField(verbose_name='number')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.PositiveBigIntegerField(verbose_name='balance')),
                ('creation_day', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Accounts', to='customer_account.customer')),
            ],
        ),
    ]
