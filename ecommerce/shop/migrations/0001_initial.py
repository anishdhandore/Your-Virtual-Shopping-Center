# Generated by Django 3.1.4 on 2021-03-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('model_name', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=200)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
