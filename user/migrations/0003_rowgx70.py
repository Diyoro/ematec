# Generated by Django 4.2.2 on 2023-06-27 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_petitmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='RowGx70',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='row_gx_70/')),
                ('texte', models.TextField()),
                ('photo_profil', models.ImageField(upload_to='row_gx_70/')),
                ('nom', models.CharField(max_length=70)),
                ('fonction', models.CharField(max_length=70)),
            ],
        ),
    ]