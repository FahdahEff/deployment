# Generated by Django 2.0.2 on 2018-04-13 19:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artName', models.CharField(default='', max_length=50)),
                ('artSize', models.CharField(default='', max_length=200)),
                ('artPrice', models.CharField(max_length=500)),
                ('artImage', models.ImageField(upload_to='media')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Artwork_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Artwork_ID', to='core.Artwork')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artwork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Artwork')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Request Name')),
                ('desc', models.CharField(max_length=500, verbose_name='Request Description')),
                ('time', models.DateTimeField(default=datetime.datetime(2018, 4, 13, 19, 5, 17, 39322, tzinfo=utc), verbose_name='Request Time')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Request_owner', to=settings.AUTH_USER_MODEL)),
                ('owner2', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='Request_owner2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artName', models.CharField(default='', max_length=50)),
                ('artSize', models.CharField(default='', max_length=200)),
                ('artPrice', models.CharField(max_length=500)),
                ('artImage', models.ImageField(upload_to='media')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ShoppingCart_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
