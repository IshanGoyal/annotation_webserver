# Generated by Django 2.0.5 on 2018-05-17 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sequence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seq_name', models.CharField(max_length=200)),
                ('blast', models.CharField(max_length=200)),
                ('pfam', models.CharField(max_length=200)),
                ('prosite', models.CharField(max_length=200)),
                ('kegg', models.CharField(max_length=200)),
                ('go', models.CharField(max_length=200)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
    ]
