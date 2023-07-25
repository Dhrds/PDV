# Generated by Django 4.0.4 on 2023-07-24 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover', models.ImageField(blank=True, default='', upload_to='covers/%Y/%m/%d/')),
                ('nome', models.TextField(max_length=255)),
                ('descricao', models.TextField(max_length=255)),
                ('preco', models.IntegerField()),
                ('categoria', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pdv.categoria')),
            ],
        ),
    ]