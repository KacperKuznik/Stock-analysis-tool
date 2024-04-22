# Generated by Django 4.2.11 on 2024-04-12 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symbols',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='klineentry',
            name='symbol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stocks.symbols'),
        ),
    ]
