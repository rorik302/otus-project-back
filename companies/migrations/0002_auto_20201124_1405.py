# Generated by Django 3.1.3 on 2020-11-24 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('types_of_companies', '0001_initial'),
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='type_of_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type_of_company', to='types_of_companies.typeofcompany'),
        ),
    ]
