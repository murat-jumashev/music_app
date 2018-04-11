# Generated by Django 2.0.4 on 2018-04-09 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('release_year', models.PositiveSmallIntegerField()),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_single', models.BooleanField(default=False)),
                ('album', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Album')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Band')),
            ],
        ),
    ]
