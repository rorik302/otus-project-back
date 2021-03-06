# Generated by Django 3.1.3 on 2020-11-24 11:18

from django.db import migrations


types_of_companies = {
    "ПAO": "Публичное акционерное общество",
    "АО": "Акционерное общество",
    "ООО": "Общество с ограниченной ответственностью"
}


def generate_types(apps, schema_editor):
    company_type = apps.get_model('types_of_companies', "TypeOfCompany")
    for k, v in types_of_companies.items():
        company_type.objects.create(
            name_short=k,
            name_full=v
        )


class Migration(migrations.Migration):

    dependencies = [
        ('types_of_companies', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(generate_types)
    ]
