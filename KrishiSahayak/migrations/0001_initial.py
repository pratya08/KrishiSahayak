# Generated by Django 3.2.4 on 2021-07-10 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=300)),
                ('pin', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=10)),
                ('productname', models.CharField(max_length=50)),
                ('productID', models.CharField(max_length=20)),
                ('quantity', models.CharField(max_length=100000)),
                ('msg', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='ShopUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopproductname', models.CharField(max_length=50)),
                ('IDproduct', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=500)),
                ('shopkeepername', models.CharField(max_length=50)),
                ('shopname', models.CharField(max_length=50)),
                ('shoplocation', models.CharField(max_length=100)),
                ('shopcontact', models.CharField(max_length=10)),
                ('postdate', models.DateTimeField()),
                ('productpic', models.ImageField()),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sfirstname', models.CharField(max_length=50)),
                ('Slastname', models.CharField(max_length=50)),
                ('Scountry', models.CharField(max_length=50)),
                ('Sstate', models.CharField(max_length=50)),
                ('Scity', models.CharField(max_length=50)),
                ('Saddress', models.CharField(max_length=300)),
                ('Spin', models.CharField(max_length=30)),
                ('Sphone', models.CharField(max_length=10)),
            ],
        ),
    ]
