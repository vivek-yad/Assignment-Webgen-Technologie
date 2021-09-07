# Generated by Django 3.1 on 2021-09-07 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=122)),
                ('lastname', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('email', models.EmailField(max_length=133)),
                ('password', models.CharField(max_length=120)),
                ('confirmpassword', models.CharField(max_length=130)),
            ],
        ),
    ]