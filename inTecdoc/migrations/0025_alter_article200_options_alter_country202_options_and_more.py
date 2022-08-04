# Generated by Django 4.0.3 on 2022-08-04 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0024_rename_country_article200_country_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article200',
            options={'verbose_name': 'Артикул', 'verbose_name_plural': 'Артикулы'},
        ),
        migrations.AlterModelOptions(
            name='country202',
            options={'verbose_name': 'Страна', 'verbose_name_plural': 'Страны'},
        ),
        migrations.AlterModelOptions(
            name='crit210',
            options={'verbose_name': 'Критерии комплектующего', 'verbose_name_plural': 'Критерии комплектующих'},
        ),
        migrations.AlterModelOptions(
            name='critval210',
            options={'verbose_name': 'Список критерий', 'verbose_name_plural': 'Критерии комплектующих'},
        ),
        migrations.AlterModelOptions(
            name='doc231and232',
            options={'verbose_name': 'Документ', 'verbose_name_plural': 'Документы'},
        ),
        migrations.AlterModelOptions(
            name='suppliers200',
            options={'verbose_name': 'Производитель комплектующей', 'verbose_name_plural': 'Производители комплектующих'},
        ),
    ]