# Generated by Django 3.2.9 on 2021-11-03 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketdata', '0004_alter_housedatapoint_mls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housedatapoint',
            name='agents',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='county',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='data_source_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='is_new_listing',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='last_update',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='line',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='lot_size_units',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='neighborhood_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='office',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='postal_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='presentation_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='prop_status',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='prop_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='property_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='rdc_web_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='state',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='state_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='time_zone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housedatapoint',
            name='units',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='housingquerydata',
            name='city',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='listofcities',
            name='city',
            field=models.TextField(),
        ),
    ]
