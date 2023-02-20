# Generated by Django 4.1.6 on 2023-02-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DomesticNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True, verbose_name='뉴스 기사 제목')),
                ('url', models.URLField(max_length=500, verbose_name='뉴스 링크')),
                ('press', models.CharField(max_length=128, verbose_name='언론사')),
                ('date', models.CharField(max_length=128, verbose_name='보도 날짜')),
            ],
            options={
                'verbose_name': '국내 뉴스',
                'verbose_name_plural': '국내 뉴스',
                'db_table': 'shinhan_DomesticNews',
            },
        ),
        migrations.CreateModel(
            name='OverseasNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True, verbose_name='뉴스 기사 제목')),
                ('url', models.URLField(max_length=500, verbose_name='뉴스 링크')),
                ('press', models.CharField(max_length=128, verbose_name='언론사')),
                ('date', models.CharField(max_length=128, verbose_name='보도 날짜')),
            ],
            options={
                'verbose_name': '해외 뉴스',
                'verbose_name_plural': '해외 뉴스',
                'db_table': 'shinhan_OverseasNews',
            },
        ),
    ]