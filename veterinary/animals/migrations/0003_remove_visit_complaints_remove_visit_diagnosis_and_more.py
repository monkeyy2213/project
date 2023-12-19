# Generated by Django 5.0 on 2023-12-19 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0002_alter_owner_options_alter_patient_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visit',
            name='complaints',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='visit',
            name='prescriptions',
        ),
        migrations.AlterField(
            model_name='providedservice',
            name='visit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.visit', verbose_name='Номер посещения'),
        ),
        migrations.CreateModel(
            name='Anamnesis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaints', models.TextField(verbose_name='Жалобы')),
                ('diagnosis', models.TextField(verbose_name='Диагноз')),
                ('prescriptions', models.TextField(verbose_name='Предписания')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.patient', verbose_name='id пациента')),
                ('visit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animals.visit', verbose_name='Номер посещения')),
            ],
            options={
                'verbose_name': 'Мед. книжка',
                'verbose_name_plural': 'Мед. книжка',
            },
        ),
    ]