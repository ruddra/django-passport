# Generated by Django 3.0.5 on 2020-04-21 13:03

from django.db import migrations, models
import passport.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', passport.users.models.CustomUserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
