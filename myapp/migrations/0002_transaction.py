# Generated by Django 5.1.3 on 2024-11-23 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gateway', models.CharField(max_length=100)),
                ('transaction_date', models.DateTimeField(default='0000-00-00 00:00:00')),
                ('account_number', models.CharField(blank=True, max_length=100, null=True)),
                ('sub_account', models.CharField(blank=True, max_length=250, null=True)),
                ('amount_in', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('amount_out', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('accumulated', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('code', models.CharField(blank=True, max_length=250, null=True)),
                ('transaction_content', models.TextField(blank=True, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'db_table': 'tb_transactions',
                'managed': True,
            },
        ),
    ]