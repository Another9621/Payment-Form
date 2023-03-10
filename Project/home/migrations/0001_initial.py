# Generated by Django 4.1.7 on 2023-02-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=1000)),
                ('email', models.CharField(max_length=50)),
                ('pincode', models.IntegerField()),
                ('cardtype', models.CharField(max_length=50)),
                ('cardnumber', models.IntegerField()),
                ('cvv', models.IntegerField()),
            ],
        ),
    ]
