# Generated by Django 2.2.28 on 2023-03-14 16:10

from typing import List, Tuple
from django.db import migrations, models
import ietf.iesg.models


class Migration(migrations.Migration):

    initial = True

    dependencies: List[Tuple[str]] = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telechat',
            fields=[
                ('telechat_id', models.IntegerField(primary_key=True, serialize=False)),
                ('telechat_date', models.DateField(blank=True, null=True)),
                ('minute_approved', models.IntegerField(blank=True, null=True)),
                ('wg_news_txt', models.TextField(blank=True)),
                ('iab_news_txt', models.TextField(blank=True)),
                ('management_issue', models.TextField(blank=True)),
                ('frozen', models.IntegerField(blank=True, null=True)),
                ('mi_frozen', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'telechat',
            },
        ),
        migrations.CreateModel(
            name='TelechatAgendaItem',
            fields=[
                ('id', models.AutoField(db_column='template_id', primary_key=True, serialize=False)),
                ('text', models.TextField(blank=True, db_column='template_text')),
                ('type', models.IntegerField(choices=[(1, 'Any Other Business (WG News, New Proposals, etc.)'), (2, 'IAB News'), (3, 'Management Item')], db_column='template_type', default=3)),
                ('title', models.CharField(db_column='template_title', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TelechatDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=ietf.iesg.models.next_telechat_date)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
