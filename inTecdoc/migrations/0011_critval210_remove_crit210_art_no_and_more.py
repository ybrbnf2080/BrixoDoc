# Generated by Django 4.0.3 on 2022-08-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0010_remove_article200_crit_no_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CritVal210',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crit_no', models.IntegerField(blank=True, null=True, verbose_name='CritNo')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='art_no',
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='crit_no',
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='description',
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='name',
        ),
        migrations.AddField(
            model_name='crit210',
            name='art_no_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inTecdoc.article200', verbose_name='art_no_crit'),
        ),
        migrations.AddField(
            model_name='crit210',
            name='crit_no_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inTecdoc.critval210', verbose_name='crit_no_crit'),
        ),
    ]
