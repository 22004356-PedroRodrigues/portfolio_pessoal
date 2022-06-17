# Generated by Django 4.0.4 on 2022-06-17 10:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_alter_post_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='TFC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=500)),
                ('autor', models.CharField(max_length=200)),
                ('ano', models.IntegerField()),
                ('imagem', models.ImageField(upload_to='')),
                ('relatorio', models.FileField(upload_to='')),
                ('github', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(default=datetime.date(2022, 6, 17)),
        ),
    ]
