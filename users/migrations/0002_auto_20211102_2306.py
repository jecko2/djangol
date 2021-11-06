# Generated by Django 3.2.9 on 2021-11-02 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuserapp',
            name='USERNAME_FIELD',
            field=models.EmailField(default=1, max_length=254, unique=True, verbose_name='email address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuserapp',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]