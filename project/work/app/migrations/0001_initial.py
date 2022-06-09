# Generated by Django 4.0.4 on 2022-05-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rangesort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage1', models.IntegerField()),
                ('storage2', models.IntegerField()),
                ('storage3', models.IntegerField()),
                ('storage4', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ReadyRangesort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w1result', models.FloatField()),
                ('w2result', models.FloatField()),
                ('w3result', models.FloatField()),
                ('w4result', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ReadyWeight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight1', models.FloatField()),
                ('weight2', models.FloatField()),
                ('weight3', models.FloatField()),
                ('weight4', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
