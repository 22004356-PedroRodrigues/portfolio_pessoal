# Generated by Django 4.0.4 on 2022-05-29 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_alter_cadeira_imagem_alter_post_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='foto',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(default=datetime.date(2022, 5, 29)),
        ),
    ]
