# Generated by Django 4.1.3 on 2022-11-10 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checker_api', '0003_advertscounter_counter'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checked_date', models.DateTimeField(verbose_name='Дата проверки')),
            ],
        ),
        migrations.RemoveField(
            model_name='advertscounter',
            name='created',
        ),
        migrations.AddField(
            model_name='advertscounter',
            name='check_date',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advert_counter', to='checker_api.checkdate', verbose_name='Дата проверки'),
        ),
    ]
