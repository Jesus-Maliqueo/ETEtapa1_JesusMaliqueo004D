# Generated by Django 3.2.3 on 2021-07-05 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_colaborador_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='colaborador',
            name='foto',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/'),
        ),
    ]
