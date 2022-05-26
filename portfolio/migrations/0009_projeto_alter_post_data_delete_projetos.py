# Generated by Django 4.0.4 on 2022-05-25 20:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_professor_alter_post_data_projetos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proj_titulo', models.CharField(max_length=100)),
                ('proj_descricao', models.CharField(max_length=100)),
                ('proj_imagem', models.ImageField(upload_to='')),
                ('proj_ano', models.CharField(max_length=100)),
                ('proj_cadeira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfolio.cadeira')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='data',
            field=models.DateField(default=datetime.date(2022, 5, 25)),
        ),
        migrations.DeleteModel(
            name='Projetos',
        ),
    ]
