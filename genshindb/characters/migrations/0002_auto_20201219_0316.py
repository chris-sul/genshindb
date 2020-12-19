# Generated by Django 3.1.3 on 2020-12-19 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillTalent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.AlterField(
            model_name='character',
            name='weapon_type',
            field=models.CharField(choices=[('bow', 'Bow'), ('catalyst', 'Catalyst'), ('claymore', 'Claymore'), ('polearm', 'Polearm'), ('sword', 'Sword')], max_length=16),
        ),
        migrations.CreateModel(
            name='NormalAttack',
            fields=[
                ('skilltalent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='characters.skilltalent')),
                ('normal', models.CharField(max_length=256)),
                ('charged', models.CharField(max_length=256)),
                ('plunging', models.CharField(max_length=256)),
                ('values', models.JSONField(default=dict)),
            ],
            bases=('characters.skilltalent',),
        ),
        migrations.AddField(
            model_name='skilltalent',
            name='character',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.character'),
        ),
    ]