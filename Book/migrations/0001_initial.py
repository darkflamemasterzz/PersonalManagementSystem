# Generated by Django 3.0.6 on 2020-05-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('book_type', models.CharField(choices=[('P', 'philosophy'), ('CS', 'computer_science'), ('N', 'novel'), ('E', 'economic'), ('O', 'other')], default='O', max_length=20)),
                ('publish_date', models.DateField()),
                ('progress', models.IntegerField(choices=[(0, '0%'), (1, '20%'), (2, '40%'), (3, '60%'), (4, '80%'), (5, '100%')], default=0)),
            ],
        ),
    ]
