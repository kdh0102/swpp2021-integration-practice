# Generated by Django 3.2.8 on 2021-10-28 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leader_set', to='hero.hero')),
                ('members', models.ManyToManyField(related_name='teams', to='hero.Hero')),
            ],
        ),
    ]
