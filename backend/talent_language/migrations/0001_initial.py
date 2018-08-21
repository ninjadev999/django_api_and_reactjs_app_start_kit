# Generated by Django 2.0.2 on 2018-08-21 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talent', '0008_auto_20180810_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='TalentLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('fluency', models.CharField(blank=True, max_length=50, null=True)),
                ('talent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talent_languages', to='talent.Talent')),
            ],
            options={
                'db_table': 'talent_language',
                'ordering': ('talent', 'language', 'fluency'),
                'managed': True,
            },
        ),
    ]
