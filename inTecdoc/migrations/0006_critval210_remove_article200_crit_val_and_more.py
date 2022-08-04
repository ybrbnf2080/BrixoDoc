# Generated by Django 4.0.3 on 2022-08-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inTecdoc', '0005_alter_article200_crit_no_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CritVal210',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crit_no', models.IntegerField(blank=True, null=True, verbose_name='CritNo')),
                ('crit_val', models.CharField(blank=True, max_length=255, null=True, verbose_name='CritVal')),
            ],
        ),
        migrations.RemoveField(
            model_name='article200',
            name='crit_val',
        ),
        migrations.RemoveField(
            model_name='crit210',
            name='crit_no',
        ),
        migrations.AddField(
            model_name='crit210',
            name='crit_no',
            field=models.ManyToManyField(blank=True, related_name='CritNo', to='inTecdoc.critval210'),
        ),
    ]