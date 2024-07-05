# Generated by Django 5.0.6 on 2024-07-05 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_modelo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='marca',
            options={'ordering': ['nome']},
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_modelo', models.IntegerField(max_length=4)),
                ('ano_fabricacao', models.IntegerField(max_length=4)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=18)),
                ('observacao', models.CharField(max_length=255)),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastro.modelo')),
            ],
        ),
    ]