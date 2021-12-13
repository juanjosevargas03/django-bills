# Generated by Django 3.2.10 on 2021-12-12 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('nit', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bills_Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('bill_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bills')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('document', models.CharField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
        migrations.AddField(
            model_name='bills_products',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.products'),
        ),
        migrations.AddField(
            model_name='bills',
            name='client_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.clients'),
        ),
    ]