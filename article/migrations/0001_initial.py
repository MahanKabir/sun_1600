# Generated by Django 3.0.2 on 2020-09-01 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('page', models.CharField(max_length=4)),
                ('price', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=45)),
                ('image', models.ImageField(upload_to='static/images/artice/')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
    ]
